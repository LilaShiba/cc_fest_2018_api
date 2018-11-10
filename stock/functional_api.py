#! /usr/bin/env python3
# Make an api call
import json, requests, datetime
# url vars
def api_url(symbol):
    # api key
    api_token = 'YOUR_API_TOKEN_HERE'
    # url
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+symbol+'&interval=1min&apikey='+api_token
    return url
# call data
def api_call(url):
    data = requests.get(url).json()
    #print(data)
    #get time now - 2 min(allow for lag) and floor
    now = datetime.datetime.now() - datetime.timedelta(minutes=2)
    now = str(now)
    now = now[:17]
    now = now + '00'
    symbol = data['Meta Data']['2. Symbol']
    high = data['Time Series (1min)'][now]['2. high']
    low = data['Time Series (1min)'][now]['3. low']
    print(symbol)
    print('high', high)
    print('low', low)
    return symbol, high, low
# main process


api_call(url)
# while loop call set on 1 min interval
