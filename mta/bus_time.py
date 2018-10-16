#! /usr/bin/env python3
# http://bustime.mta.info/wiki/Developers/Index
import requests, json, re, urllib.parse

station = input("what station: bb for brooklyn bridge OR br for bay ridge: ")
station = station.replace(" ", "")
if station == 'bb' or station =="BB":
	station = "308204"
	#"change last char for direction"
elif station == 'br' or station =='BR':
	station = "305423"
else:
	print ("error")

#Call subway time data
api_token = "YOUR_API_TOKEN_HERE"
url = "http://bustime.mta.info/api/siri/stop-monitoring.json?key="+api_token+"&OperatorRef=MTA&MonitoringRef="+station+"&LineRef=MTA NYCT_B63&MaximumStopVisits=2"

#Parse Subway times
data = requests.get(url).json()
progress = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['ProgressRate']
name = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['LineRef']
time = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime']
#distance = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
stops = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['StopsFromCall']
stops = str(stops)
bus_stop = data['Siri']['ServiceDelivery']['StopMonitoringDelivery'][0]['MonitoredStopVisit'][0]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']

# regrex for time
times = re.compile(r'\d\d:\d\d')
short_time = times.findall(time)

#regrex for bus
short_bus_name = re.compile("[a-zA-Z]\d{2}")
bus_name_results = short_bus_name.findall(name)

#print(data)
print("Bus " + bus_name_results[0] +" is "+ stops + " stops away from " + bus_stop)
print("Route Info: " + progress)
print("ETA: " + short_time[0])
