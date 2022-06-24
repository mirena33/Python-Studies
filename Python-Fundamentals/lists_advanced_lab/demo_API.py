import requests

# api key
key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# request data from url
data = requests.get(key)
data = data.json()

print(f"{data['symbol']} price is {data['price']}")
