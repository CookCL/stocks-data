# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import pandas as pd
import datetime as dt

aggdict = {
    'open':'first',
    'high':'max',
    'low':'min',
    'close':'last',
    'volume':'sum'
}

 def HigherTimeframeResample(source , newFreq ='5min'):
        df = source.groupby(pd.Grouper(level=0, freq= newFreq, label='left')).agg(aggdict)
        return df

# ### Read in data
# Data source: Tradestation export

# +
#Read from .txt in Tradestation format
df = pd.read_csv("SPY_1min.txt")

#Create volume column
df['volume'] = df['Up'] + df['Down']

#Rename columns
df = df.rename(columns={
    'Open': 'open',
    'High': 'high',
    'Low': 'low',
    'Close': 'close'})

#Convert strings of date and time to datetime format
df["datetime"] = df["Date"] + " " + df["Time"]
df["datetime"] =pd.to_datetime(df["datetime"])

#Shift 1min to the left for proper higher timeframe generation
df["datetime"] = df["datetime"] - dt.timedelta(minutes=1)
df= df.set_index('datetime')

#drop unneccessary columns
df = df.drop(columns=['Date', 'Time', 'Up', 'Down'])
# -

# ### Create higher timeframe dataframes

bars1m = df
bars5m = HigherTimeframeResample(bars1m, newFreq='5min')
bars30m = HigherTimeframeResample(bars1m, newFreq='30min')
bars1h = HigherTimeframeResample(bars1m, newFreq='1h')

bars1m

bars5m

bars30m

bars1h

nbconvert — to script TimeframeResample.ipynb
