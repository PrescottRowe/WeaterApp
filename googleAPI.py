import requests                         #request information from a webpage
import json				#for using/parsing json files

class GoogleAPICaller:

    def __init__(self, key):
        self._key = key
        self._formattedAddress = '' #the complete address of the location (for example, in case the user only enters the zip code and not the whole address)
        self._longitude = ''
        self._latitude = ''
        
    def setAddress(self, address):
        locationJsonData = self.getLocationJsonData(address)
        self._formattedAddress = locationJsonData['results'][0]['formatted_address']
        self._longitude = locationJsonData['results'][0]['geometry']['location']['lng']
        self._latitude = locationJsonData['results'][0]['geometry']['location']['lat']
        
    
    def getLocationJsonData(self, address):
            googleAPI = 'https://maps.googleapis.com/maps/api/geocode/json?&address='
            address = "%20".join(address.split(" "))	#format the address so that it can be used with googleAPI. It replaces the space char with "%20"
            googleAPI = googleAPI + address + '&key=' + self._key
            locationJsonData  = requests.get(googleAPI).json()
            return locationJsonData


    # returns the complete address of the location (for example, in case the user only enters the zip code and not the whole address)
    def getFormattedAddress(self):
            return self._formattedAddress

    def getLongitude(self):
            return self._longitude

    def getLatitude(self):
            return self._latitude

    def printAddress_Long_Lat(self):
        print(self.getFormattedAddress())
        print("long:", self.getLongitude(), "lat:", self.getLatitude())

        

    #autocomplete example for springfield that eliminates ambiguity by returning several results that may match the user's input
    #https://maps.googleapis.com/maps/api/place/autocomplete/json?parameters&key=AIzaSyAqoxRyeH5P6_PWTJ5QLXr_vB6ZOQ4l8zo&input=springfield
