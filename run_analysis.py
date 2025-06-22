import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Removed pandas_ta imports
import matplotlib.dates as mdates
import os
from datetime import time

# --- Global Parameters for Backtesting (from backtest.py) ---
PROFIT_TARGET_PCT = 0.015  # 1.5%
STOP_LOSS_PCT = 0.010     # 1.0%
RSI_OVERBOUGHT = 75
RSI_OVERSOLD = 25
MAX_TRADES_PER_DAY = 5 # Increased for more potential signals in short timeframe
ENTRY_CUTOFF_TIME = time(15, 30) # No entries after 3:30 PM
EXIT_TIME = time(15, 55)      # Exit all positions by 3:55 PM

# --- P&L Modeling Parameters (from backtest.py, simplified for this task) ---
COMMISSION_PER_TRADE = 1.00 # Simplified to a flat $1 per trade for underlying

# --- Manual Indicator Implementations ---

def calculate_vwap(df_group):
    # VWAP for a single day group
    return (df_group['average'] * df_group['volume']).cumsum() / df_group['volume'].cumsum()

def calculate_ema(series, length):
    return series.ewm(span=length, adjust=False).mean()

def calculate_rsi(series, length=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=length).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=length).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def load_and_prepare_data(csv_filepath="QQQ_1min_data_with_indicators.csv"):
    """Loads data, converts date column, and calculates necessary indicators."""
    print(f"Loading data from {csv_filepath}...")
    df = pd.read_csv(csv_filepath)

    # Convert 'date' column to datetime and set as index
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')

    print("Calculating VWAP, EMAs, and RSI manually...")

    # Check if 'average' column exists for VWAP, if not, use typical price
    if 'average' not in df.columns:
        print("'average' column not found for VWAP, using (high+low+close)/3 as typical price.")
        df['average'] = (df['high'] + df['low'] + df['close']) / 3

    # Calculate VWAP (anchored daily)
    df['VWAP_D'] = df.groupby(df.index.date, group_keys=False).apply(calculate_vwap)

    # Calculate EMAs for Strategy 1 & 3
    df['EMA_5'] = calculate_ema(df['close'], length=5) # For Strategy 3
    df['EMA_9'] = calculate_ema(df['close'], length=9)  # For Strategy 1
    df['EMA_10'] = calculate_ema(df['close'], length=10) # For Strategy 3
    df['EMA_21'] = calculate_ema(df['close'], length=21) # For Strategy 1

    # Use existing RSI_14 from CSV (for Strategy 1 & 2), handle potential typo 'Rsi_14'.
    # If RSI_14 is missing entirely, then calculate it.
    if 'RSI_14' not in df.columns:
        if 'Rsi_14' in df.columns:
            df.rename(columns={'Rsi_14': 'RSI_14'}, inplace=True)
            print("Using existing RSI_14 column from CSV (renamed from Rsi_14).")
        else:
            print("RSI_14 column not found, calculating manually.")
            df['RSI_14'] = calculate_rsi(df['close'], length=14)
    else:
        print("Using existing RSI_14 column from CSV.")

    # Drop rows with NaN values that might have been created by indicator calculations
    # Especially important for rolling calculations like RSI and initial EMA values.
    df.dropna(inplace=True)
    print("Data loaded and indicators calculated.")
    print("Columns available:", df.columns.tolist())
    # print(df[['close', 'VWAP_D', 'EMA_9', 'EMA_21', 'RSI_14']].head())
    return df

def run_backtest(df: pd.DataFrame, strategy_config: dict):
    """
    Runs the backtest on the DataFrame with indicators based on the provided strategy config.
    """
    strategy_name = strategy_config['name']
    print(f"\nRunning backtest for Strategy: {strategy_name}...")

    trades = []
    in_position = False
    entry_price = 0.0
    stop_loss_price = 0.0
    profit_target_price = 0.0
    position_type = None # 'long' or 'short'
    entry_time = None

    # Get strategy-specific parameters
    profit_target_pct = strategy_config.get('PROFIT_TARGET_PCT', PROFIT_TARGET_PCT)
    stop_loss_pct = strategy_config.get('STOP_LOSS_PCT', STOP_LOSS_PCT)
    rsi_overbought = strategy_config.get('RSI_OVERBOUGHT', RSI_OVERBOUGHT)
    rsi_oversold = strategy_config.get('RSI_OVERSOLD', RSI_OVERSOLD)
    rsi_confirm_level_long = strategy_config.get('RSI_CONFIRM_LEVEL_LONG')
    rsi_confirm_level_short = strategy_config.get('RSI_CONFIRM_LEVEL_SHORT')

    daily_trade_counts = {}

    for i in range(1, len(df)):
        current_row = df.iloc[i]
        prev_row = df.iloc[i-1]

        current_date = current_row.name.date()
        if current_date not in daily_trade_counts:
            daily_trade_counts[current_date] = 0

        # --- Exit Logic (remains mostly the same, uses potentially strategy-specific PT/SL) ---
        if in_position:
            exit_signal_triggered = False
            exit_reason = ""
            # Profit Target
            if position_type == 'long' and current_row['high'] >= profit_target_price:
                exit_price = profit_target_price
                exit_signal_triggered = True
                exit_reason = "Profit Target"
            elif position_type == 'short' and current_row['low'] <= profit_target_price:
                exit_price = profit_target_price
                exit_signal_triggered = True
                exit_reason = "Profit Target"

            # Stop Loss
            if not exit_signal_triggered:
                if position_type == 'long' and current_row['low'] <= stop_loss_price:
                    exit_price = stop_loss_price
                    exit_signal_triggered = True
                    exit_reason = "Stop Loss"
                elif position_type == 'short' and current_row['high'] >= stop_loss_price:
                    exit_price = stop_loss_price
                    exit_signal_triggered = True
                    exit_reason = "Stop Loss"

            # Time-Based Exit / End of day for current trade
            # Ensure position is closed if it's the last bar for the entry day or EXIT_TIME is reached
            is_last_bar_of_entry_day = (i == len(df) - 1) or (current_row.name.date() != entry_time.date())

            if not exit_signal_triggered and (current_row.name.time() >= EXIT_TIME or is_last_bar_of_entry_day):
                exit_price = current_row['close']
                exit_signal_triggered = True
                exit_reason = "End of Day / Time Exit" if current_row.name.time() >= EXIT_TIME else "End of Day Data"


            if exit_signal_triggered:
                pnl_underlying = (exit_price - entry_price) if position_type == 'long' else (entry_price - exit_price)
                # Simple PNL, not percentage based for commission here
                pnl_net = pnl_underlying - COMMISSION_PER_TRADE

                trades.append({
                    'entry_time': entry_time, 'exit_time': current_row.name,
                    'entry_price': entry_price, 'exit_price': exit_price,
                    'pnl_underlying': pnl_underlying, 'pnl_net': pnl_net,
                    'type': position_type, 'exit_reason': exit_reason
                })
                in_position = False
                position_type = None

        # --- Entry Logic ---
        if not in_position and daily_trade_counts[current_date] < MAX_TRADES_PER_DAY and current_row.name.time() < ENTRY_CUTOFF_TIME:
            long_signal = False
            short_signal = False

            # --- Apply Strategy Rules ---
            if strategy_name == "VWAP_EMA_RSI":
                if pd.notna(prev_row['VWAP_D']) and pd.notna(current_row['VWAP_D']) and \
                   pd.notna(current_row['EMA_9']) and pd.notna(current_row['EMA_21']) and pd.notna(current_row['RSI_14']):
                    if (prev_row['close'] <= prev_row['VWAP_D']) and \
                       (current_row['close'] > current_row['VWAP_D']) and \
                       (current_row['EMA_9'] > current_row['EMA_21']) and \
                       (current_row['RSI_14'] < rsi_overbought):
                        long_signal = True
                    elif (prev_row['close'] >= prev_row['VWAP_D']) and \
                         (current_row['close'] < current_row['VWAP_D']) and \
                         (current_row['EMA_9'] < current_row['EMA_21']) and \
                         (current_row['RSI_14'] > rsi_oversold):
                        short_signal = True

            elif strategy_name == "MACD_RSI":
                # Ensure MACD columns exist and are not NaN
                if pd.notna(prev_row['MACD_12_26_9']) and pd.notna(prev_row['MACDs_12_26_9']) and \
                   pd.notna(current_row['MACD_12_26_9']) and pd.notna(current_row['MACDs_12_26_9']) and \
                   pd.notna(current_row['RSI_14']):

                    # Long: MACD crosses above Signal, RSI > confirm level
                    if (prev_row['MACD_12_26_9'] <= prev_row['MACDs_12_26_9']) and \
                       (current_row['MACD_12_26_9'] > current_row['MACDs_12_26_9']) and \
                       (current_row['RSI_14'] > rsi_confirm_level_long):
                        long_signal = True
                    # Short: MACD crosses below Signal, RSI < confirm level
                    elif (prev_row['MACD_12_26_9'] >= prev_row['MACDs_12_26_9']) and \
                         (current_row['MACD_12_26_9'] < current_row['MACDs_12_26_9']) and \
                         (current_row['RSI_14'] < rsi_confirm_level_short):
                        short_signal = True

            elif strategy_name == "EMA_CROSS":
                 if pd.notna(prev_row['EMA_5']) and pd.notna(prev_row['EMA_10']) and \
                    pd.notna(current_row['EMA_5']) and pd.notna(current_row['EMA_10']):
                    # Long: Fast EMA crosses above Slow EMA
                    if (prev_row['EMA_5'] <= prev_row['EMA_10']) and \
                       (current_row['EMA_5'] > current_row['EMA_10']):
                        long_signal = True
                    # Short: Fast EMA crosses below Slow EMA
                    elif (prev_row['EMA_5'] >= prev_row['EMA_10']) and \
                         (current_row['EMA_5'] < current_row['EMA_10']):
                        short_signal = True

            if long_signal:
                in_position = True
                position_type = 'long'
                entry_price = current_row['close']
                entry_time = current_row.name
                profit_target_price = entry_price * (1 + profit_target_pct)
                stop_loss_price = entry_price * (1 - stop_loss_pct)
                daily_trade_counts[current_date] += 1
            elif short_signal:
                in_position = True
                position_type = 'short'
                entry_price = current_row['close']
                entry_time = current_row.name
                profit_target_price = entry_price * (1 - profit_target_pct)
                stop_loss_price = entry_price * (1 + stop_loss_pct)
                daily_trade_counts[current_date] += 1

    print(f"Backtest for {strategy_name} complete. Total trades simulated: {len(trades)}")
    if not trades:
        print(f"No trades were executed for {strategy_name}.")
        return pd.DataFrame()

    trades_df = pd.DataFrame(trades)
    return trades_df

def generate_trade_intuition(trades_df, original_data_df, strategy_config):
    """
    Generates a markdown file with intuition for each trade for a specific strategy.
    """
    strategy_name = strategy_config['name']
    print(f"\nGenerating trade intuition file for {strategy_name}...")

    # Ensure the main directory exists
    os.makedirs("trading_analysis_results", exist_ok=True)

    filepath = f"trading_analysis_results/trade_intuition_{strategy_name}.md"
    with open(filepath, "w") as f:
        f.write(f"# Strategy: {strategy_name} - Trade Rationale and Indicator States\n\n")
        f.write("## Strategy Rules:\n")
        for rule_line in strategy_config['rules_doc']:
            f.write(f"- {rule_line}\n")
        f.write("\n---\n\n")

        for index, trade in trades_df.iterrows():
            f.write(f"## Trade {index + 1}: {trade['type'].upper()} at {trade['entry_time']}\n\n")
            f.write(f"- **Entry Time:** {trade['entry_time']}\n")
            f.write(f"- **Entry Price:** {trade['entry_price']:.2f}\n")
            f.write(f"- **Trade Type:** {trade['type']}\n")
            f.write(f"- **Exit Time:** {trade['exit_time']}\n")
            f.write(f"- **Exit Price:** {trade['exit_price']:.2f}\n")
            f.write(f"- **Exit Reason:** {trade['exit_reason']}\n")
            f.write(f"- **PnL (Underlying):** {trade['pnl_underlying']:.2f}\n\n")

            # Get indicator states at entry time from the original DataFrame
            # Need to find the row in original_data_df that corresponds to trade['entry_time']
            # The index of original_data_df is datetime, so direct lookup should work.
            try:
                entry_data_row = original_data_df.loc[trade['entry_time']]
                # Find the previous row for prev_close vs prev_vwap condition check
                entry_idx = original_data_df.index.get_loc(trade['entry_time'])
                if entry_idx > 0:
                    prev_entry_data_row = original_data_df.iloc[entry_idx - 1]
                else: # Should not happen if backtest starts from index 1 of df_qqq
                    prev_entry_data_row = None

                f.write("### Indicator States at Entry:\n")
                f.write(f"- **Current Close:** {entry_data_row['close']:.2f}\n")
                f.write(f"- **Current VWAP_D:** {entry_data_row['VWAP_D']:.2f}\n")
                if prev_entry_data_row is not None and pd.notna(prev_entry_data_row['VWAP_D']):
                    f.write(f"- **Previous Close:** {prev_entry_data_row['close']:.2f}\n")
                    f.write(f"- **Previous VWAP_D:** {prev_entry_data_row['VWAP_D']:.2f}\n")
                else:
                    f.write("- Previous VWAP_D or Close: Not available (likely first valid bar for backtest)\n")

                f.write(f"- **EMA_9:** {entry_data_row['EMA_9']:.2f}\n")
                f.write(f"- **EMA_21:** {entry_data_row['EMA_21']:.2f}\n")
                f.write(f"- **RSI_14:** {entry_data_row['RSI_14']:.2f}\n\n")

                f.write("### Entry Rationale:\n")
                rationale = f"Entered {trade['type']} because: \n"
                if trade['type'] == 'long':
                    if prev_entry_data_row is not None and pd.notna(prev_entry_data_row['VWAP_D']):
                        rationale += f"- Previous Close ({prev_entry_data_row['close']:.2f}) was <= Previous VWAP_D ({prev_entry_data_row['VWAP_D']:.2f}).\n"
                    rationale += f"- Current Close ({entry_data_row['close']:.2f}) crossed > Current VWAP_D ({entry_data_row['VWAP_D']:.2f}).\n"
                    rationale += f"- EMA_9 ({entry_data_row['EMA_9']:.2f}) was > EMA_21 ({entry_data_row['EMA_21']:.2f}).\n"
                    rationale += f"- RSI_14 ({entry_data_row['RSI_14']:.2f}) was < Overbought threshold ({RSI_OVERBOUGHT}).\n"
                elif trade['type'] == 'short':
                    if prev_entry_data_row is not None and pd.notna(prev_entry_data_row['VWAP_D']):
                        rationale += f"- Previous Close ({prev_entry_data_row['close']:.2f}) was >= Previous VWAP_D ({prev_entry_data_row['VWAP_D']:.2f}).\n"
                    rationale += f"- Current Close ({entry_data_row['close']:.2f}) crossed < Current VWAP_D ({entry_data_row['VWAP_D']:.2f}).\n"
                    rationale += f"- EMA_9 ({entry_data_row['EMA_9']:.2f}) was < EMA_21 ({entry_data_row['EMA_21']:.2f}).\n"
                    rationale += f"- RSI_14 ({entry_data_row['RSI_14']:.2f}) was > Oversold threshold ({RSI_OVERSOLD}).\n"
                f.write(rationale)
            except KeyError:
                f.write("Could not retrieve indicator data for this trade's entry time.\n")
            f.write("\n---\n\n")
    print(f"Trade intuition file generated at {filepath}")

def plot_trades_for_day(daily_data, trades_on_day, date_str, strategy_name, strategy_config):
    """
    Plots price, indicators, and trades for a single day for a specific strategy.
    """
    fig, ax1 = plt.subplots(figsize=(15, 8))

    # Plot price
    ax1.plot(daily_data.index, daily_data['close'], label='Close Price', color='skyblue', linewidth=1.5)
    ax1.set_xlabel('Time (US/Eastern)')
    ax1.set_ylabel('Price ($)', color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')
    indicators_to_plot = strategy_config.get('indicators_to_plot', [])

    # Plot specified indicators
    if 'EMA_9' in indicators_to_plot and 'EMA_9' in daily_data.columns:
        ax1.plot(daily_data.index, daily_data['EMA_9'], label='EMA(9)', color='orange', linestyle='--', linewidth=1)
    if 'EMA_21' in indicators_to_plot and 'EMA_21' in daily_data.columns:
        ax1.plot(daily_data.index, daily_data['EMA_21'], label='EMA(21)', color='purple', linestyle='--', linewidth=1)
    if 'EMA_5' in indicators_to_plot and 'EMA_5' in daily_data.columns:
        ax1.plot(daily_data.index, daily_data['EMA_5'], label='EMA(5)', color='yellow', linestyle='--', linewidth=1)
    if 'EMA_10' in indicators_to_plot and 'EMA_10' in daily_data.columns:
        ax1.plot(daily_data.index, daily_data['EMA_10'], label='EMA(10)', color='pink', linestyle='--', linewidth=1)
    if 'VWAP_D' in indicators_to_plot and 'VWAP_D' in daily_data.columns:
        ax1.plot(daily_data.index, daily_data['VWAP_D'], label='VWAP_D', color='gray', linestyle=':', linewidth=1.2)

    if 'MACD_12_26_9' in indicators_to_plot and 'MACD_12_26_9' in daily_data.columns:
         ax1.plot(daily_data.index, daily_data['MACD_12_26_9'], label='MACD', color='blue', linestyle='-', linewidth=0.8, alpha=0.7)
    if 'MACDs_12_26_9' in indicators_to_plot and 'MACDs_12_26_9' in daily_data.columns:
         ax1.plot(daily_data.index, daily_data['MACDs_12_26_9'], label='Signal Line', color='red', linestyle='--', linewidth=0.8, alpha=0.7)

    # Plot buy signals
    buy_signals = trades_on_day[trades_on_day['type'] == 'long']
    ax1.scatter(buy_signals['entry_time'], buy_signals['entry_price'] * 0.998, # Slightly below price
                marker='^', color='green', s=150, label='Buy Signal', zorder=5)
    # Plot sell signals for exits of long trades
    # ax1.scatter(buy_signals['exit_time'], buy_signals['exit_price'],
    #             marker='v', color='darkgreen', s=100, label='Sell to Close Long', zorder=5)


    # Plot short sell signals
    sell_signals = trades_on_day[trades_on_day['type'] == 'short']
    ax1.scatter(sell_signals['entry_time'], sell_signals['entry_price'] * 1.002, # Slightly above price
                marker='v', color='red', s=150, label='Short Sell Signal', zorder=5)
    # Plot buy to cover signals for exits of short trades
    # ax1.scatter(sell_signals['exit_time'], sell_signals['exit_price'],
    #             marker='^', color='darkred', s=100, label='Buy to Cover Short', zorder=5)

    # Create a second y-axis for RSI
    ax2 = ax1.twinx()
    ax2.plot(daily_data.index, daily_data['RSI_14'], label='RSI(14)', color='brown', linestyle='-.', linewidth=0.8, alpha=0.7)
    ax2.set_ylabel('RSI', color='brown')
    ax2.tick_params(axis='y', labelcolor='brown')
    ax2.axhline(RSI_OVERBOUGHT, color='red', linestyle='--', linewidth=0.5, alpha=0.5)
    ax2.axhline(RSI_OVERSOLD, color='green', linestyle='--', linewidth=0.5, alpha=0.5)
    ax2.set_ylim(0, 100)

    # Formatting
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    plt.title(f'QQQ Trades and Indicators - {date_str}')

    # Combine legends
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(lines + lines2, labels + labels2, loc='upper left')

    ax1.grid(True, linestyle=':', alpha=0.7)
    fig.tight_layout()

    # Ensure strategy-specific plot directory exists
    plot_subdir = f"trading_analysis_results/plots/{strategy_name}"
    os.makedirs(plot_subdir, exist_ok=True)
    plot_filename = f"{plot_subdir}/trades_{date_str}.png"

    plt.savefig(plot_filename)
    print(f"Plot saved: {plot_filename}")
    plt.close(fig)


if __name__ == '__main__':
    # Create main results directory first
    os.makedirs("trading_analysis_results", exist_ok=True)
    os.makedirs("trading_analysis_results/plots", exist_ok=True)

    df_qqq_original = load_and_prepare_data()

    if df_qqq_original.empty:
        print("Failed to load or prepare data. Exiting.")
    else:
        print("\nSample of prepared data (with all indicators for all strategies):")
        # Displaying a broader set of columns for verification
        cols_to_show = ['close', 'VWAP_D', 'EMA_5', 'EMA_9', 'EMA_10', 'EMA_21', 'RSI_14', 'MACD_12_26_9', 'MACDs_12_26_9']
        cols_present = [col for col in cols_to_show if col in df_qqq_original.columns]
        print(df_qqq_original[cols_present].head())

        print(f"\nData shape: {df_qqq_original.shape}")
        print(f"\nData covers period from {df_qqq_original.index.min()} to {df_qqq_original.index.max()}")

        strategy1_config = {
            'name': "VWAP_EMA_RSI",
            'PROFIT_TARGET_PCT': 0.015, 'STOP_LOSS_PCT': 0.010,
            'RSI_OVERBOUGHT': 75, 'RSI_OVERSOLD': 25,
            'indicators_to_plot': ['VWAP_D', 'EMA_9', 'EMA_21', 'RSI_14'],
            'rules_doc': [
                "Strategy: VWAP crossover confirmed by EMA crossover and RSI not in extreme zone.",
                "Long Entry: Previous Close <= Previous VWAP_D AND Current Close > Current VWAP_D AND EMA_9 > EMA_21 AND RSI_14 < 75.",
                "Short Entry: Previous Close >= Previous VWAP_D AND Current Close < Current VWAP_D AND EMA_9 < EMA_21 AND RSI_14 > 25.",
                "Exits: 1.5% Profit Target, 1.0% Stop Loss, or End-of-Day/Session."
            ]
        }

        strategy2_config = {
            'name': "MACD_RSI",
            'PROFIT_TARGET_PCT': 0.012, 'STOP_LOSS_PCT': 0.008,
            'RSI_CONFIRM_LEVEL_LONG': 50, 'RSI_CONFIRM_LEVEL_SHORT': 50, # RSI must be above 50 for long, below 50 for short
            'indicators_to_plot': ['RSI_14', 'MACD_12_26_9', 'MACDs_12_26_9'],
            'rules_doc': [
                "Strategy: MACD Crossover with RSI confirmation.",
                "Long Entry: MACD line crosses above Signal line AND RSI_14 > 50.",
                "Short Entry: MACD line crosses below Signal line AND RSI_14 < 50.",
                "Exits: 1.2% Profit Target, 0.8% Stop Loss, or End-of-Day/Session."
            ]
        }

        strategy3_config = {
            'name': "EMA_CROSS",
            'PROFIT_TARGET_PCT': 0.010, 'STOP_LOSS_PCT': 0.007,
            'indicators_to_plot': ['EMA_5', 'EMA_10', 'RSI_14'], # Added RSI for context in plot
            'rules_doc': [
                "Strategy: Simple Fast EMA (5) crossing Slow EMA (10).",
                "Long Entry: EMA_5 crosses above EMA_10.",
                "Short Entry: EMA_5 crosses below EMA_10.",
                "Exits: 1.0% Profit Target, 0.7% Stop Loss, or End-of-Day/Session."
            ]
        }

        strategies = [strategy1_config, strategy2_config, strategy3_config]
        all_available_dates = sorted(list(df_qqq_original.index.normalize().unique()))

        overall_summary_content = "# Trading Strategies Performance Summary\n\n"

        for config in strategies:
            strategy_name = config['name']

            # Create strategy-specific plot directory
            plot_dir = f"trading_analysis_results/plots/{strategy_name}"
            os.makedirs(plot_dir, exist_ok=True)

            # It's crucial to pass a copy of the DataFrame if the backtest function might modify it,
            # or ensure the backtest function doesn't modify the input df in place.
            # For this implementation, run_backtest doesn't modify df, but copy is safer.
            trades_df = run_backtest(df_qqq_original.copy(), config)

            total_pnl = trades_df['pnl_net'].sum() if not trades_df.empty else 0.0
            num_trades = len(trades_df)

            overall_summary_content += f"## Strategy: {strategy_name}\n"
            overall_summary_content += f"- Total Net PnL (after $1 commission per trade): {total_pnl:.2f}\n"
            overall_summary_content += f"- Total Trades: {num_trades}\n\n"

            if not trades_df.empty:
                print(f"\nTrades Log for {strategy_name}:")
                print(trades_df.head())
                trades_df.to_csv(f"trading_analysis_results/trades_log_{strategy_name}.csv", index=False)
                print(f"Trades log for {strategy_name} saved to trading_analysis_results/trades_log_{strategy_name}.csv")

                generate_trade_intuition(trades_df, df_qqq_original, config)

                print(f"\nGenerating trade visualization plots for {strategy_name}...")
                # Ensure entry_time is datetime for proper comparison
                trades_df['entry_time'] = pd.to_datetime(trades_df['entry_time'])

                for plot_date_ts in all_available_dates: # plot_date_ts is a Timestamp
                    plot_date = plot_date_ts.date() # Convert to date object for comparisons
                    date_str = plot_date.strftime('%Y-%m-%d')

                    daily_data_to_plot = df_qqq_original[df_qqq_original.index.date == plot_date]
                    trades_on_this_day = trades_df[trades_df['entry_time'].dt.date == plot_date]

                    if not daily_data_to_plot.empty:
                        print(f"Plotting for {strategy_name} - day: {date_str}")
                        plot_trades_for_day(daily_data_to_plot, trades_on_this_day, date_str, strategy_name, config)
                    else:
                        print(f"No data to plot for {strategy_name} - day: {date_str}")
            else:
                print(f"No trades were generated by the backtest for {strategy_name}.")
                # Still generate an intuition file with rules even if no trades
                generate_trade_intuition(pd.DataFrame(), df_qqq_original, config)


        with open("trading_analysis_results/strategies_summary.md", "w") as f:
            f.write(overall_summary_content)
        print("\nOverall strategies summary saved to trading_analysis_results/strategies_summary.md")

def generate_trade_intuition(trades_df, original_data_df):
    """
    Generates a markdown file with intuition for each trade.
    """
    print("\nGenerating trade intuition file...")
    filepath = "trading_analysis_results/trade_intuition.md"
    with open(filepath, "w") as f:
        f.write("# Trade Entry Rationale and Indicator States\n\n")
        for index, trade in trades_df.iterrows():
            f.write(f"## Trade {index + 1}: {trade['type'].upper()} at {trade['entry_time']}\n\n")
            f.write(f"- **Entry Time:** {trade['entry_time']}\n")
            f.write(f"- **Entry Price:** {trade['entry_price']:.2f}\n")
            f.write(f"- **Trade Type:** {trade['type']}\n")
            f.write(f"- **Exit Time:** {trade['exit_time']}\n")
            f.write(f"- **Exit Price:** {trade['exit_price']:.2f}\n")
            f.write(f"- **Exit Reason:** {trade['exit_reason']}\n")
            f.write(f"- **PnL (Underlying):** {trade['pnl_underlying']:.2f}\n\n")

            # Get indicator states at entry time from the original DataFrame
            # Need to find the row in original_data_df that corresponds to trade['entry_time']
            # The index of original_data_df is datetime, so direct lookup should work.
            try:
                entry_data_row = original_data_df.loc[trade['entry_time']]
                # Find the previous row for prev_close vs prev_vwap condition check
                entry_idx = original_data_df.index.get_loc(trade['entry_time'])
                if entry_idx > 0:
                    prev_entry_data_row = original_data_df.iloc[entry_idx - 1]
                else: # Should not happen if backtest starts from index 1 of df_qqq
                    prev_entry_data_row = None

                f.write("### Indicator States at Entry:\n")
                f.write(f"- **Current Close:** {entry_data_row['close']:.2f}\n")
                f.write(f"- **Current VWAP_D:** {entry_data_row['VWAP_D']:.2f}\n")
                if prev_entry_data_row is not None and pd.notna(prev_entry_data_row['VWAP_D']):
                    f.write(f"- **Previous Close:** {prev_entry_data_row['close']:.2f}\n")
                    f.write(f"- **Previous VWAP_D:** {prev_entry_data_row['VWAP_D']:.2f}\n")
                else:
                    f.write("- Previous VWAP_D or Close: Not available (likely first valid bar for backtest)\n")

                f.write(f"- **EMA_9:** {entry_data_row['EMA_9']:.2f}\n")
                f.write(f"- **EMA_21:** {entry_data_row['EMA_21']:.2f}\n")
                f.write(f"- **RSI_14:** {entry_data_row['RSI_14']:.2f}\n\n")

                f.write("### Entry Rationale:\n")
                rationale = f"Entered {trade['type']} because: \n"
                if trade['type'] == 'long':
                    if prev_entry_data_row is not None and pd.notna(prev_entry_data_row['VWAP_D']):
                        rationale += f"- Previous Close ({prev_entry_data_row['close']:.2f}) was <= Previous VWAP_D ({prev_entry_data_row['VWAP_D']:.2f}).\n"
                    rationale += f"- Current Close ({entry_data_row['close']:.2f}) crossed > Current VWAP_D ({entry_data_row['VWAP_D']:.2f}).\n"
                    rationale += f"- EMA_9 ({entry_data_row['EMA_9']:.2f}) was > EMA_21 ({entry_data_row['EMA_21']:.2f}).\n"
                    rationale += f"- RSI_14 ({entry_data_row['RSI_14']:.2f}) was < Overbought threshold ({RSI_OVERBOUGHT}).\n"
                elif trade['type'] == 'short':
                    if prev_entry_data_row is not None and pd.notna(prev_entry_data_row['VWAP_D']):
                        rationale += f"- Previous Close ({prev_entry_data_row['close']:.2f}) was >= Previous VWAP_D ({prev_entry_data_row['VWAP_D']:.2f}).\n"
                    rationale += f"- Current Close ({entry_data_row['close']:.2f}) crossed < Current VWAP_D ({entry_data_row['VWAP_D']:.2f}).\n"
                    rationale += f"- EMA_9 ({entry_data_row['EMA_9']:.2f}) was < EMA_21 ({entry_data_row['EMA_21']:.2f}).\n"
                    rationale += f"- RSI_14 ({entry_data_row['RSI_14']:.2f}) was > Oversold threshold ({RSI_OVERSOLD}).\n"
                f.write(rationale)
            except KeyError:
                f.write("Could not retrieve indicator data for this trade's entry time.\n")
            f.write("\n---\n\n")
    print(f"Trade intuition file generated at {filepath}")
