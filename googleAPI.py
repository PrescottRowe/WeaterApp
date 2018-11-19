import requests  # requests information from a webpage
import json

class GoogleAPICaller:

    def __init__(self, key):
        self._key = key
        self._formattedAddress = ''  # the complete address of the location (for example, in case the user only enters the zip code and not the whole address)
        self._longitude = ''
        self._latitude = ''
        self._locationJsonData = ''

    # sets the JsonData based on the address provided
    def setJsonData(self, address):
        self._locationJsonData = self.getLocationJsonData(address)

    # use this after setJsonData to check if the provided address is legitimate
    def checkIfValidAddress(self):
        if self._locationJsonData['status'] == 'OK':
            return True
        else:
            return False

    def setAddress(self):
        self._formattedAddress = self._locationJsonData['results'][0]['formatted_address']
        self._longitude = self._locationJsonData['results'][0]['geometry']['location']['lng']
        self._latitude = self._locationJsonData['results'][0]['geometry']['location']['lat']

    def getLocationJsonData(self, address):
        googleAPI = 'https://maps.googleapis.com/maps/api/geocode/json?&address='
        address = "%20".join(address.split(" "))  # format the address so that it can be used with googleAPI. It replaces the space char with "%20"
        googleAPI = googleAPI + address + '&key=' + self._key
        locationJsonData = requests.get(googleAPI).json()
        return locationJsonData

    # returns the complete address of the location (for example, in case the user only enters the zip code and not the whole address)
    def getFormattedAddress(self):
        return self._formattedAddress

    def getLongitude(self):
        return self._longitude

    def getLatitude(self):
        return self._latitude

    # returns a list of possible locations based on the user input (this is the prediction texts that will be displayed under the text field)
    # this should only be called when the user enters/deletes a set number of chars (maybe at least 3)
    # DO NOT call this function after each char is entered/deleted since it will make an API call each time
    # returns a list containing possible locations
    def predictLocation(self, address):
        googleAPI = 'https://maps.googleapis.com/maps/api/place/autocomplete/json?parameters&key='
        address = "%20".join(address.split(
            " "))  # format the address so that it can be used with googleAPI. It replaces the space char with "%20"
        googleAPI = googleAPI + self._key + '&input=' + address
        predictionJsonData = requests.get(googleAPI).json()
        predictionList = list()
        if predictionJsonData['status'] == 'OK':
            for location in predictionJsonData['predictions']:
                predictionList.append(location['description'])
            return predictionList

    # autocomplete example for springfield that eliminates ambiguity by returning several results that may match the user's input
    # https://maps.googleapis.com/maps/api/place/autocomplete/json?parameters&key=key&input=springfield
