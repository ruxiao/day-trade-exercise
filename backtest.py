import os
import pandas as pd
import pandas_ta as ta
import numpy as np
from datetime import datetime, timedelta, time
from polygon import RESTClient

# --- Part 1: Data Fetching ---
def get_qqq_data(api_key: str, months_of_data: int = 6) -> pd.DataFrame:
    """
    Fetches historical 1-minute aggregate bar data for QQQ for the past specified number of months from Polygon.io.
    """
    client = RESTClient(api_key)
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=months_of_data * 30)
    print(f"Fetching 1-minute QQQ data from {start_date} to {end_date}...")
    try:
        aggs = client.list_aggs("QQQ", 1, "minute", start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), limit=50000)
        df = pd.DataFrame(list(aggs))
        if df.empty:
            print("No data returned.")
            return pd.DataFrame()
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df.set_index('timestamp')
        df = df[['open', 'high', 'low', 'close', 'volume']]
        df.index = df.index.tz_localize('UTC').tz_convert('US/Eastern')
        print(f"Successfully fetched {len(df)} rows of data.")
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

# --- Part 2: Indicator Calculation ---
def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates all necessary technical indicators and appends them to the DataFrame.
    """
    print("Calculating technical indicators...")
    # VWAP (anchored to daily session)
    df.ta.vwap(anchor="D", append=True)
    # EMAs
    df.ta.ema(length=9, append=True)
    df.ta.ema(length=21, append=True)
    # RSI
    df.ta.rsi(length=14, append=True)
    
    # Clean up NaN values created by indicators
    df.dropna(inplace=True)
    print("Indicators calculated and NaN rows dropped.")
    return df

# --- Part 3 & 4: Backtesting Engine ---
def run_backtest(df: pd.DataFrame):
    """
    Runs the vectorized backtest on the DataFrame with indicators.
    """
    print("Running backtest...")
    
    # --- Strategy Parameters ---
    PROFIT_TARGET_PCT = 0.015  # 1.5%
    STOP_LOSS_PCT = 0.010     # 1.0%
    RSI_OVERBOUGHT = 75
    RSI_OVERSOLD = 25
    MAX_TRADES_PER_DAY = 5
    ENTRY_CUTOFF_TIME = time(15, 30)
    EXIT_TIME = time(15, 55)
    
    # --- P&L Modeling Parameters ---
    OPTION_DELTA = 0.5
    COMMISSION_PER_TRADE = 1.00 # $1 round-trip commission/slippage

    # --- State Variables ---
    in_position = False
    entry_price = 0.0
    stop_loss_price = 0.0
    profit_target_price = 0.0
    daily_trade_count = 0
    last_trade_date = None
    
    trades =
    
    # --- Backtesting Loop ---
    for i in range(1, len(df)):
        current_row = df.iloc[i]
        prev_row = df.iloc[i-1]
        
        # Reset daily trade counter at the start of a new day
        current_date = current_row.name.date()
        if last_trade_date!= current_date:
            daily_trade_count = 0
        last_trade_date = current_date

        # --- Exit Logic ---
        if in_position:
            # Check for Profit Target
            if current_row['high'] >= profit_target_price:
                exit_price = profit_target_price
                pnl_underlying = exit_price - entry_price if position_type == 'long' else entry_price - exit_price
                trades.append({'entry_time': entry_time, 'exit_time': current_row.name, 'entry_price': entry_price, 'exit_price': exit_price, 'pnl_underlying': pnl_underlying, 'type': position_type})
                in_position = False
                continue
            # Check for Stop Loss
            elif current_row['low'] <= stop_loss_price:
                exit_price = stop_loss_price
                pnl_underlying = exit_price - entry_price if position_type == 'long' else entry_price - exit_price
                trades.append({'entry_time': entry_time, 'exit_time': current_row.name, 'entry_price': entry_price, 'exit_price': exit_price, 'pnl_underlying': pnl_underlying, 'type': position_type})
                in_position = False
                continue
            # Check for Time-Based Exit
            elif current_row.name.time() >= EXIT_TIME:
                exit_price = current_row['close']
                pnl_underlying = exit_price - entry_price if position_type == 'long' else entry_price - exit_price
                trades.append({'entry_time': entry_time, 'exit_time': current_row.name, 'entry_price': entry_price, 'exit_price': exit_price, 'pnl_underlying': pnl_underlying, 'type': position_type})
                in_position = False
                continue

        # --- Entry Logic ---
        if not in_position and daily_trade_count < MAX_TRADES_PER_DAY and current_row.name.time() < ENTRY_CUTOFF_TIME:
            # Long Entry Condition
            if (prev_row['close'] <= prev_row) and (current_row['close'] > current_row) and \
               (current_row['EMA_9'] > current_row['EMA_21']) and (current_row < RSI_OVERBOUGHT):
                in_position = True
                position_type = 'long'
                entry_price = current_row['close']
                entry_time = current_row.name
                profit_target_price = entry_price * (1 + PROFIT_TARGET_PCT)
                stop_loss_price = entry_price * (1 - STOP_LOSS_PCT)
                daily_trade_count += 1
                
            # Short Entry Condition
            elif (prev_row['close'] >= prev_row) and (current_row['close'] < current_row) and \
                 (current_row['EMA_9'] < current_row['EMA_21']) and (current_row > RSI_OVERSOLD):
                in_position = True
                position_type = 'short'
                entry_price = current_row['close']
                entry_time = current_row.name
                profit_target_price = entry_price * (1 + STOP_LOSS_PCT) # Reversed for short
                stop_loss_price = entry_price * (1 - PROFIT_TARGET_PCT) # Reversed for short
                daily_trade_count += 1

    print(f"Backtest complete. Total trades simulated: {len(trades)}")
    
    if not trades:
        print("No trades were executed.")
        return None
        
    # --- Performance Calculation ---
    trades_df = pd.DataFrame(trades)
    
    # Calculate P&L percentage for underlying
    trades_df['pnl_underlying_pct'] = (trades_df['pnl_underlying'] / trades_df['entry_price'])
    
    # Model option P&L
    trades_df['pnl_option_pct'] = trades_df['pnl_underlying_pct'] * OPTION_DELTA
    
    # Model commission cost (as a percentage of a hypothetical $10,000 position)
    trades_df['commission_pct'] = COMMISSION_PER_TRADE / 10000
    
    # Final Net P&L
    trades_df['net_pnl_pct'] = trades_df['pnl_option_pct'] - trades_df['commission_pct']
    
    return trades_df

def analyze_performance(trades_df: pd.DataFrame, initial_capital=10000):
    """
    Analyzes the performance of the backtest and prints key metrics.
    """
    if trades_df is None or trades_df.empty:
        print("No trades to analyze.")
        return

    total_trades = len(trades_df)
    wins = trades_df[trades_df['net_pnl_pct'] > 0]
    losses = trades_df[trades_df['net_pnl_pct'] <= 0]
    
    win_rate = len(wins) / total_trades if total_trades > 0 else 0
    avg_win_pct = wins['net_pnl_pct'].mean()
    avg_loss_pct = losses['net_pnl_pct'].mean()
    profit_factor = abs(wins['net_pnl_pct'].sum() / losses['net_pnl_pct'].sum()) if losses['net_pnl_pct'].sum()!= 0 else float('inf')
    
    # Calculate equity curve and drawdown
    trades_df['cumulative_pnl_pct'] = trades_df['net_pnl_pct'].cumsum()
    trades_df['equity_curve'] = initial_capital * (1 + trades_df['cumulative_pnl_pct'])
    
    running_max = trades_df['equity_curve'].expanding().max()
    drawdown = (trades_df['equity_curve'] - running_max) / running_max
    max_drawdown = drawdown.min()
    
    total_net_pnl = trades_df['equity_curve'].iloc[-1] - initial_capital
    total_net_pnl_pct = total_net_pnl / initial_capital
    
    # Simplified Sharpe Ratio (assuming risk-free rate is 0)
    # Note: A proper Sharpe requires daily returns, this is an approximation.
    daily_returns = trades_df.set_index('exit_time')['net_pnl_pct'].resample('D').sum()
    sharpe_ratio = (daily_returns.mean() / daily_returns.std()) * np.sqrt(252) if daily_returns.std()!= 0 else 0

    # --- Print Results ---
    print("\n--- Backtest Performance Summary ---")
    print(f"Total Net P&L: ${total_net_pnl:,.2f} ({total_net_pnl_pct:.2%})")
    print(f"Sharpe Ratio (annualized approx.): {sharpe_ratio:.2f}")
    print(f"Maximum Drawdown: {max_drawdown:.2%}")
    print(f"Profit Factor: {profit_factor:.2f}")
    print(f"Total Trades: {total_trades}")
    print(f"Win Rate: {win_rate:.2%}")
    print(f"Average Win: {avg_win_pct:.2%}")
    print(f"Average Loss: {avg_loss_pct:.2%}")

if __name__ == '__main__':
    # It is recommended to store your API key as an environment variable
    # For example: export POLYGON_API_KEY='YourKey'
    polygon_api_key = os.getenv("POLYGON_API_KEY")
    
    if not polygon_api_key:
        print("Error: POLYGON_API_KEY environment variable not set.")
    else:
        # 1. Fetch Data
        qqq_df = get_qqq_data(api_key=polygon_api_key, months_of_data=6)
        
        if not qqq_df.empty:
            # 2. Calculate Indicators
            data_with_indicators = calculate_indicators(qqq_df)
            
            # 3. Run Backtest
            results_df = run_backtest(data_with_indicators)
            
            # 4. Analyze Performance
            if results_df is not None:
                analyze_performance(results_df)