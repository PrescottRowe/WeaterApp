import requests                         #request information from a webpage
import json				#for using/parsing json files
from datetime import datetime           #for turning unixtime to human-readable time


_weatherIcons = ["clear-day","clear-night","partly-cloudy-day","partly-cloudy-night","cloudy","rain","sleet","snow","wind","fog"]
_degree_sign= u'\N{DEGREE SIGN}'

class DarkSkyAPICaller:
    def __init__(self, key):
        self._key = key

        #for current forecast (Today)
        self._currentSummary = ''
        self._currentIcon = ''
        self._currentTemp = ''
        self._currentLowTemp = ''
        self._currentHighTemp = ''
        

        #for weekly forecast
        self._weeklyWeatherIcon = []
        self._weeklyTempHigh = []
        self._weeklyTempLow = []
        self._weeklySummary = []
        self._weeklyUnixTime = []        
        self._date = []        

        
        
    def getForecastJsonData(self, latitude, longitude):
        darkskyAPI = 'https://api.darksky.net/forecast/' + self._key + '/' + str(latitude) + ',' + str(longitude)
        #print("darksky key " + darkskyAPI)
        forecastJsonData = requests.get(darkskyAPI).json()
        return forecastJsonData

    def setCurrentForecast(self, forecastJsonData):
        currentForecast = forecastJsonData['currently']
        self._currentSummary = currentForecast['summary']
        self._currentIcon = currentForecast['icon']
        self._currentTemp = str(round(currentForecast['temperature'])) + _degree_sign
        currentForecast = forecastJsonData['daily']
        self._currentLowTemp = str(round(currentForecast['data'][0]['temperatureLow'])) + _degree_sign 
        self._currentHighTemp = str(round(currentForecast['data'][0]['temperatureHigh'])) + _degree_sign

    

    def setWeeklyForecast(self, forecastJsonData):
        weeklyForecastList = forecastJsonData['daily']      #the 'daily' key in the Json data contains the weekly forecast
        i = 0                                               #used to skip the first entry of the weekly forecast, which is the current day. This is to remove redundancy since setCurrentForecast already gets the forecast for the current day
        for k,v in weeklyForecastList.items():              #iterate through each key and value pair in the Json data
            if k == 'data':                                 #data contains weather info for each day of the week
                for day in weeklyForecastList['data']:
                    if i != 0:                              #if day isn't today                   
                        self._weeklyUnixTime.append(day['time'])
                        self._weeklySummary.append(day['summary'])
                        self._weeklyWeatherIcon.append(day['icon'])
                        self._weeklyTempHigh.append( str(round(day['temperatureHigh'])) + _degree_sign)
                        self._weeklyTempLow.append( str(round(day['temperatureLow'])) + _degree_sign)
                    i+=1
    
    

    def printWeeklyForecast(self):
        print("Today")
        print(self._currentTemp, self._currentSummary)
        print("Low:", self._currentLowTemp, "High:",self._currentHighTemp)
        print("Icon:", self._currentIcon)
        print()

        for i in range(len(self._weeklyUnixTime)):
            day = datetime.fromtimestamp(self._weeklyUnixTime[i]).strftime("%A")
            print(day)
            value = datetime.fromtimestamp(self._weeklyUnixTime[i])
            date = value.strftime('%Y-%m-%d')
            print(date)
            #print(self._weeklyUnixTime[i])
            print(self._weeklySummary[i])
            print("Low:", self._weeklyTempLow[i], "High:",self._weeklyTempHigh[i])
            print("Icon:", self._weeklyWeatherIcon[i], '\n')

    
    
