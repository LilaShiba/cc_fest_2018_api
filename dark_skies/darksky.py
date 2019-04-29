#! /usr/bin/env python3
# Dark Sky Doc: https://darksky.net/dev
import json, requests

############################### API Request Parameters #########################################################################
api_token = 'your key here'
lat = '40.7128'
lon = '-74.0060'
url = 'https://api.darksky.net/forecast/'+api_token+'/'+lat+','+lon
#print(url)
############################### Make API Call #########################################################################
data = requests.get(url).json()
#print(data)
############################### Parse API Data #########################################################################

current = data['currently']
summary = current['summary']
temp = current['temperature']
wind = current['windSpeed']
uv = current['uvIndex']
min_cast = data['minutely']['data'][0]
min_sum = data['minutely']['summary']
daily = data['daily']['data'][0]
moon = daily['moonPhase']


############################### Print Out Parsed Data #########################################################################


print(min_sum)
print('The temp is ' + str(temp))
print('The wind is blowing at ' + str(wind))
print('UV index is at ' + str(uv))
print('The moon is at ' + str(moon))
