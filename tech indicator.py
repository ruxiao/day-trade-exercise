# Assuming 'df' is the DataFrame with OHLCV data
# The 'anchor="D"' parameter ensures the VWAP resets daily.
df.ta.vwap(anchor="D", append=True)
# Calculate the 9-period and 21-period EMAs and append them to the DataFrame
df.ta.ema(length=9, append=True)
df.ta.ema(length=21, append=True)
# Calculate the 14-period RSI and append it to the DataFrame
df.ta.rsi(length=14, append=True)