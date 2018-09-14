'''
CUI soon to be GUI 9/10/18
Enter a US only zip code or type a city and state and get a weekly forcast of the weather.
This program calls on the national weather service API and the Google API for geo cords. To use this you will need your own api key from google.
Written by Fredson Laguna, Prescott Rowe, Justin Hartline
'''

import requests                         #request information from a webpage
import json				#for using/parsing json files


# returns jsonData based on the api request
def spider(api_request):
    url = 'https://api.weather.gov' + str(api_request)
    jsonData = requests.get(url).json()
    return jsonData


def callLocationAPI(address):
	googleAPI = 'https://maps.googleapis.com/maps/api/geocode/json?&address='
	apiKey = 'VeryNiceKeyMuchMeowGoesHere' #Key required to use google API. 
	address = "+".join(address.split(" "))	#format the address so that it can be used with googleAPI. It replaces the space char with "+"
	googleAPI = googleAPI + address + '&key=' + apiKey
	locationJsonData = requests.get(googleAPI).json()
	return locationJsonData

# returns the complete address of the location (for example, in case the user only enters the zip code and not the whole address)
# input must be the json type returned from function callLocationAPI(address)
def getFormattedAddress(locationJsonData):
	return locationJsonData['results'][0]['formatted_address']

# returns the longitude
# input must be the json type returned from function callLocationAPI(address)
def getLongitude(locationJsonData):
	return locationJsonData['results'][0]['geometry']['location']['lng']

# returns the latitude
# input must be the json type returned from function callLocationAPI(address)
def getLatitude(locationJsonData):
	return locationJsonData['results'][0]['geometry']['location']['lat']

# returns json that includes information about the given point
# this is required since the json file that this function returns contains api calls for both weekly forecast AND hourly forecast
def getEndpoint(latitude, longitude):
	api_request = '/points/' + str(latitude) + ',' + str(longitude)
	return spider(api_request)




def main():
    address = input("Enter address information: ")
    print("\n")
    locationJsonData = callLocationAPI(address)
    formattedAddress = getFormattedAddress(locationJsonData)
    longitude = getLongitude(locationJsonData)
    latitude = getLatitude(locationJsonData)
    print("long: " + str(longitude) + "\nlatitude: " + str(latitude)+ "\n")
    print("The weather for " + formattedAddress + " is: \n")
    #jsonData = spider('/points/33.7343,-117.185') #used for testing/sanity check
    jsonData = getEndpoint(latitude, longitude)
    weeklyForecastAPICall = jsonData['properties']['forecast'].replace("https://api.weather.gov", "")
    jsonData = spider(weeklyForecastAPICall)
    weeklyForecastList = jsonData['properties']['periods']
    for i in range(0,len(weeklyForecastList)):
        print(weeklyForecastList[i]['name'] + '\n')
        print(weeklyForecastList[i]['detailedForecast'] + '\n\n')


if __name__ == '__main__': main()

