import requests
import pandas as pd
URL = 'https://api.kraken.com/0/public/OHLC'
payloads = {'pair': 'xmrusd'}
r = requests.get(URL, params=payloads)
data = r.json()
df = pd.DataFrame.from_dict(data['result']['XXMRZUSD'])
print(data['result']['XXMRZUSD'])
df.columns = ['timestamp', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'count']
df.to_csv('xmrreult.csv', index=False)