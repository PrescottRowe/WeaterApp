from googleAPI import GoogleAPICaller
from darkskyAPI import DarkSkyAPICaller
from forecast import Forecast
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty


class SearchScreen(Screen):
    location = StringProperty('No location')

    def set_location(self, address):
        self.location = str(address)
        self.manager.current = "ForecastScreen"


class ForecastScreen(Screen):
    label_location = StringProperty('')
    address = StringProperty('')
    cTime = StringProperty('')
    cTemp = StringProperty('')
    cIcon = StringProperty('')
    cSummary = StringProperty('')
    cHumidity = StringProperty('')
    cUVIndex = StringProperty('')
    cOzone = StringProperty('')
    cWindSpeed = StringProperty('')
    cWindGust = StringProperty('')
    cVisibility = StringProperty('')

    def get_data(self):
        isAddressLegit=False
        while isAddressLegit == False:
            googleAPICaller.setJsonData(self.label_location)
            isAddressLegit = googleAPICaller.checkIfValidAddress()
            if isAddressLegit == True:
                predictionList = googleAPICaller.predictLocation(self.label_location)
                address = predictionList[0]
                googleAPICaller.setJsonData(address)
                googleAPICaller.setAddress()

        latitude = googleAPICaller.getLatitude()
        longitude = googleAPICaller.getLongitude()
        forecastData = darkSkyAPICaller.getForecastJsonData(latitude, longitude)
        formattedAddress = googleAPICaller.getFormattedAddress()
        self.fcast = Forecast(forecastData, formattedAddress)

        self.address = str(self.fcast.address)
        self.cTime = str(self.fcast.cTime)
        self.cTemp = str(self.fcast.cTemp)
        self.cIcon = str(self.fcast.cIcon)
        self.cSummary = str(self.fcast.cSummary)
        self.cHumidity = str(self.fcast.cHumidity)
        self.cUVIndex= str(self.fcast.cUVIndex)
        self.cOzone = str(self.fcast.cOzone)
        self.cWindSpeed = str(self.fcast.cWindSpeed)
        self.cWindGust = str(self.fcast.cWindGust)
        self.cVisibility = str(self.fcast.cVisi)


googleKey = ''
darkSkyKey = ''
googleAPICaller = GoogleAPICaller(googleKey)
darkSkyAPICaller = DarkSkyAPICaller(darkSkyKey)
sm=Builder.load_file('weather.kv')
class WeatherApp(App):#app class must match kv file minus "app"
    def build(self):#pass the instance of the class to the function so it knows it parent.
        return sm

if __name__ == "__main__":#only autorun the code if the file is being run as main.
    WeatherApp().run()



