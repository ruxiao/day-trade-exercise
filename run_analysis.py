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

    # Calculate EMAs
    df['EMA_9'] = calculate_ema(df['close'], length=9)
    df['EMA_21'] = calculate_ema(df['close'], length=21)

    # Use existing RSI_14 from CSV, handle potential typo 'Rsi_14'.
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

def run_backtest(df: pd.DataFrame):
    """
    Runs the vectorized backtest on the DataFrame with indicators.
    """
    print("Running backtest...")

    trades = []
    in_position = False
    entry_price = 0.0
    stop_loss_price = 0.0
    profit_target_price = 0.0
    position_type = None # 'long' or 'short'
    entry_time = None

    # Initialize daily trade counter
    daily_trade_counts = {} # Dictionary to store trade counts for each day

    for i in range(1, len(df)):
        current_row = df.iloc[i]
        prev_row = df.iloc[i-1]

        current_date = current_row.name.date()
        if current_date not in daily_trade_counts:
            daily_trade_counts[current_date] = 0

        # --- Exit Logic ---
        if in_position:
            exit_signal_triggered = False
            exit_reason = ""
            # Check for Profit Target
            if position_type == 'long' and current_row['high'] >= profit_target_price:
                exit_price = profit_target_price
                exit_signal_triggered = True
                exit_reason = "Profit Target"
            elif position_type == 'short' and current_row['low'] <= profit_target_price: # Reversed for short
                exit_price = profit_target_price
                exit_signal_triggered = True
                exit_reason = "Profit Target"

            # Check for Stop Loss
            if not exit_signal_triggered:
                if position_type == 'long' and current_row['low'] <= stop_loss_price:
                    exit_price = stop_loss_price
                    exit_signal_triggered = True
                    exit_reason = "Stop Loss"
                elif position_type == 'short' and current_row['high'] >= stop_loss_price: # Reversed for short
                    exit_price = stop_loss_price
                    exit_signal_triggered = True
                    exit_reason = "Stop Loss"

            # Check for Time-Based Exit or if it's the last bar of the day
            if not exit_signal_triggered and (current_row.name.time() >= EXIT_TIME or i == len(df) - 1 or current_row.name.date() != df.iloc[i-1].name.date()):
                exit_price = current_row['close']
                exit_signal_triggered = True
                exit_reason = "End of Day / Time Exit"

            if exit_signal_triggered:
                pnl_underlying = (exit_price - entry_price) if position_type == 'long' else (entry_price - exit_price)
                pnl_net = pnl_underlying - (COMMISSION_PER_TRADE / entry_price) # Commission as fraction of entry

                trades.append({
                    'entry_time': entry_time,
                    'exit_time': current_row.name,
                    'entry_price': entry_price,
                    'exit_price': exit_price,
                    'pnl_underlying': pnl_underlying,
                    'pnl_net': pnl_net,
                    'type': position_type,
                    'exit_reason': exit_reason
                })
                in_position = False
                position_type = None
                # Continue to check for new entry signals on the same bar if exit occurred early
                # but only if we haven't hit the daily trade limit for the *next* trade.
                # This check is effectively done before entry logic.

        # --- Entry Logic ---
        # Check if we can enter a new position
        can_enter_trade = (
            not in_position and
            daily_trade_counts[current_date] < MAX_TRADES_PER_DAY and
            current_row.name.time() < ENTRY_CUTOFF_TIME
        )

        if can_enter_trade:
            # Long Entry Condition
            # prev_row['close'] <= prev_row['VWAP_D'] might be problematic if VWAP_D is NaN for prev_row
            # Ensure prev_row has valid VWAP_D
            if pd.notna(prev_row['VWAP_D']) and pd.notna(current_row['VWAP_D']):
                if (prev_row['close'] <= prev_row['VWAP_D']) and \
                   (current_row['close'] > current_row['VWAP_D']) and \
                   (current_row['EMA_9'] > current_row['EMA_21']) and \
                   (current_row['RSI_14'] < RSI_OVERBOUGHT):

                    in_position = True
                    position_type = 'long'
                    entry_price = current_row['close']
                    entry_time = current_row.name
                    profit_target_price = entry_price * (1 + PROFIT_TARGET_PCT)
                    stop_loss_price = entry_price * (1 - STOP_LOSS_PCT)
                    daily_trade_counts[current_date] += 1
                    # No continue here, an exit might occur on the same bar if targets are very tight

                # Short Entry Condition (elif to prevent flip-flop on same bar if logic allows)
                elif (prev_row['close'] >= prev_row['VWAP_D']) and \
                     (current_row['close'] < current_row['VWAP_D']) and \
                     (current_row['EMA_9'] < current_row['EMA_21']) and \
                     (current_row['RSI_14'] > RSI_OVERSOLD):

                    in_position = True
                    position_type = 'short'
                    entry_price = current_row['close']
                    entry_time = current_row.name
                    profit_target_price = entry_price * (1 - PROFIT_TARGET_PCT) # Correct for short
                    stop_loss_price = entry_price * (1 + STOP_LOSS_PCT)     # Correct for short
                    daily_trade_counts[current_date] += 1


    print(f"Backtest complete. Total trades simulated: {len(trades)}")

    if not trades:
        print("No trades were executed.")
        return pd.DataFrame() # Return empty DataFrame

    trades_df = pd.DataFrame(trades)
    return trades_df

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

def plot_trades_for_day(daily_data, trades_on_day, date_str):
    """
    Plots price, indicators, and trades for a single day.
    """
    fig, ax1 = plt.subplots(figsize=(15, 8))

    # Plot price
    ax1.plot(daily_data.index, daily_data['close'], label='Close Price', color='skyblue', linewidth=1.5)
    ax1.set_xlabel('Time (US/Eastern)')
    ax1.set_ylabel('Price ($)', color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')

    # Plot EMAs
    ax1.plot(daily_data.index, daily_data['EMA_9'], label='EMA(9)', color='orange', linestyle='--', linewidth=1)
    ax1.plot(daily_data.index, daily_data['EMA_21'], label='EMA(21)', color='purple', linestyle='--', linewidth=1)

    # Plot VWAP
    ax1.plot(daily_data.index, daily_data['VWAP_D'], label='VWAP_D', color='gray', linestyle=':', linewidth=1.2)

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

    plot_filename = f"trading_analysis_results/plots/trades_{date_str}.png"
    plt.savefig(plot_filename)
    print(f"Plot saved: {plot_filename}")
    plt.close(fig)


if __name__ == '__main__':
    df_qqq = load_and_prepare_data()
    if not df_qqq.empty:
        print("\nSample of prepared data:")
        print(df_qqq[['close', 'VWAP_D', 'EMA_9', 'EMA_21', 'RSI_14']].head())
        print(f"\nData shape: {df_qqq.shape}")
        print(f"\nData covers period from {df_qqq.index.min()} to {df_qqq.index.max()}")

        # Create results directory
        os.makedirs("trading_analysis_results", exist_ok=True)
        os.makedirs("trading_analysis_results/plots", exist_ok=True) # Changed this line

        trades_df = run_backtest(df_qqq)
        if not trades_df.empty:
            print("\nTrades Log:")
            print(trades_df)
            trades_df.to_csv("trading_analysis_results/trades_log.csv", index=False)
            print("\nTrades log saved to trading_analysis_results/trades_log.csv")

            # Generate Trade Intuition File
            generate_trade_intuition(trades_df, df_qqq)

            # Generate Plots for each day with trades
            print("\nGenerating trade visualization plots...")
            if not trades_df.empty:
                # Ensure entry_time is datetime for proper comparison
                trades_df['entry_time'] = pd.to_datetime(trades_df['entry_time'])

                trade_dates = sorted(list(trades_df['entry_time'].dt.date.unique()))
                all_data_dates = sorted(list(df_qqq.index.normalize().unique()))

                # Plot for all days in the data, highlighting trades if they exist on that day
                for plot_date in all_data_dates:
                    date_str = plot_date.strftime('%Y-%m-%d')
                    # Correctly filter daily_data_to_plot using .date() for comparison
                    daily_data_to_plot = df_qqq[df_qqq.index.date == plot_date.date()]
                    trades_on_this_day = trades_df[trades_df['entry_time'].dt.date == plot_date.date()]

                    if not daily_data_to_plot.empty:
                        print(f"Plotting for day: {date_str}")
                        plot_trades_for_day(daily_data_to_plot, trades_on_this_day, date_str)
                    else:
                        print(f"No data to plot for day: {date_str}")
            else:
                # If no trades, still plot daily charts if desired, or just skip
                print("No trades to visualize on plots. Plotting daily data without trade markers.")
                all_data_dates = sorted(list(df_qqq.index.normalize().unique()))
                for plot_date in all_data_dates:
                    date_str = plot_date.strftime('%Y-%m-%d')
                    daily_data_to_plot = df_qqq[df_qqq.index.date == plot_date]
                    if not daily_data_to_plot.empty:
                        print(f"Plotting for day: {date_str}")
                        plot_trades_for_day(daily_data_to_plot, pd.DataFrame(), date_str) # Empty trades df
                    else:
                        print(f"No data to plot for day: {date_str}")

        else:
            print("No trades were generated by the backtest.")

    else:
        print("Failed to load or prepare data.")

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
