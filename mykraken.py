import requests
import pandas as pd
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

URL = 'https://api.kraken.com/0/public/OHLC'
payloads = {'pair': 'xmrusd'}
r = requests.get(URL, params=payloads)
data = r.json()

df = pd.DataFrame.from_dict(data['result']['XXMRZUSD'])
print(data['result']['XXMRZUSD'])
df[4] = df[4].astype(float)

df.columns = ['timestamp', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'count']
df['datetime'] = [datetime.fromtimestamp(x) for x in df['timestamp']]
df['open'] = df['open'].astype(float)
df['oc'] = df['open']-df['close']

df.to_csv("{0}-{1}.csv".format(payloads['pair'], datetime.today().strftime('%Y-%m-%d-%H-%M-%S')), index=False)

#filters
b, a = signal.butter(3, 0.05)
df['filter'] = signal.filtfilt(b, a, df['close'])

plt.figure(figsize=(20, 8))
plt.rcParams["date.autoformatter.minute"] = "%Y-%m-%d %H:%M:%S"
plt.plot(df['datetime'], df['close'], alpha=.3)
plt.plot(df['datetime'], df['filter'])


plt.show()