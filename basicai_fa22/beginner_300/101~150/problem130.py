import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

x = float(btc['max_price']) - float(btc['min_price'])
y = float(btc['opening_price'])
z = float(btc['max_price'])

if (y+x) > z:
    print("상승장")
else:
    print("하락장")