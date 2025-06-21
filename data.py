import os
import pandas as pd
from datetime import datetime, timedelta
from polygon import RESTClient

def get_qqq_data(api_key: str, months_of_data: int = 6) -> pd.DataFrame:
    """
    Fetches historical 1-minute aggregate bar data for QQQ for the past specified number of months.

    Args:
        api_key (str): Your Polygon.io API key.
        months_of_data (int): The number of months of historical data to fetch.

    Returns:
        pd.DataFrame: A DataFrame containing the OHLCV data with a DatetimeIndex.
    """
    # Initialize the REST Client
    client = RESTClient(api_key)

    # Calculate the date range for the past 6 months
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=months_of_data * 30)

    print(f"Fetching 1-minute QQQ data from {start_date} to {end_date}...")

    try:
        # The list_aggs method returns a generator; we iterate through it to build a list of bars
        aggs = client.list_aggs(
            ticker="QQQ",
            multiplier=1,
            timespan="minute",
            from_=start_date.strftime('%Y-%m-%d'),
            to=end_date.strftime('%Y-%m-%d'),
            limit=50000  # Max limit per request
        )
        
        # Convert the generator to a list of dictionaries
        all_aggs = list(aggs)
        
        if not all_aggs:
            print("No data returned from API. Check your API key and date range.")
            return pd.DataFrame()

        # Convert the list of aggregate objects to a pandas DataFrame
        df = pd.DataFrame(all_aggs)
        
        # Convert timestamp (nanoseconds) to a readable datetime format and set as index
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df = df.set_index('timestamp')
        
        # Ensure the columns are in the standard OHLCV format
        df = df[['open', 'high', 'low', 'close', 'volume']]
        
        # Polygon data is typically in UTC, convert to Eastern Time for market context
        df.index = df.index.tz_localize('UTC').tz_convert('US/Eastern')
        
        print(f"Successfully fetched {len(df)} rows of data.")
        return df

    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        return pd.DataFrame()

# Example usage (replace 'YOUR_API_KEY' with your actual key)
# polygon_api_key = os.getenv("POLYGON_API_KEY", "YOUR_API_KEY")
# qqq_df = get_qqq_data(api_key=polygon_api_key)
# if not qqq_df.empty:
#     print(qqq_df.head())
#     print(qqq_df.tail())