#! /usr/bin/env python3
# http://datamine.mta.info/
import requests, json, urllib.parse

# get input data
station = input("what station: w/h: ")
station = station.replace(" ", "")
if station == 'w' or station =="W":
	station = "121S"
	#"change last char for direction"
elif station == 'h' or station =='H':
	station = "D25N"
else:
	print ("error")
time = input("What time do you want to leave: ")
time_end = input("what's the latest time to leave: ")

#Call subway time data
url = "http://mtaapi.herokuapp.com/api?id="+station

#Parse Subway times
data = requests.get(url).json()

#Results
name = data['result']['name']
arrivals = data['result']['arrivals']
times = sorted(arrivals)

print(name)
for x in times:
	if x > time and x < time_end:
		print(x)
