import requests                         #request information from a webpage
import json				#for using/parsing json files

_weatherIcons = ["default", "clear-day","clear-night","partly-cloudy-day","partly-cloudy-night","cloudy","rain","sleet","snow","wind","fog"]

class DarkSkyAPICaller:
    def __init__(self, key):
        self._key = key
      
    def getForecastJsonData(self, latitude, longitude):
        darkskyAPI = 'https://api.darksky.net/forecast/' + self._key + '/' + str(latitude) + ',' + str(longitude)
        #print("darksky key " + darkskyAPI)
        forecastJsonData = requests.get(darkskyAPI).json()
        return forecastJsonData
