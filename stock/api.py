#! /usr/bin/env python3
# https://www.alphavantage.co/documentation/
# Make an api call
import json, requests, datetime
#url vars
# api key
api_token = 'YOUR_API_TOKEN_HERE'
# url
boeing = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=BA&interval=1min&apikey='+api_token
apple = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=1min&apikey='+api_token

# call data
data = requests.get(apple).json()
#print(data)
#get time now - 2 min(allow for lag) and floor
now = datetime.datetime.now() - datetime.timedelta(minutes=2)
# turn into string for api url
now = str(now)
# knock off milli seconds
now = now[:17]
# floor seconds
now = now + '00'

# parsing data
symbol = data['Meta Data']['2. Symbol']
today = data['Time Series (1min)']['2018-10-11 13:59:00']
high = data['Time Series (1min)'][now]['2. high']
low = data['Time Series (1min)'][now]['3. low']
print(symbol)
print('high', high)
print('low', low)
