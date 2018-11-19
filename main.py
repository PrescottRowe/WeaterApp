#__version__ = "1.2"
import kivy
kivy.require('1.9.1')
from googleAPI import GoogleAPICaller
from darkskyAPI import DarkSkyAPICaller
from forecast import Forecast
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.core.window import Window
from datetime import datetime


class SearchScreen(Screen):
    location = StringProperty('No location')

    def set_location(self, address):
        self.location = str(address)
        self.manager.current = "ForecastScreen"
        sm.transition.direction = 'left'


class ForecastScreen(Screen):
    UvLvl = {0:"Very Low", 1:"Very Low", 2:"Low", 3:"Low", 4:"Normal", 5:"Normal", 6:"High",
             7:"Very High", 8:"Damaging", 9:"Dangerous", 10:"Dangerous"}
    VisLvl = {10:"Very High", 9:"High", 8:"Good", 7:"Okay", 6:"Sub-par", 5:"Bad", 4:"Bad",
              3:"Terrible", 2:"Terrible", 1:"Dangerous", 0:"Dangerous" }
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
    dTime0 = StringProperty('')
    dIcon0 = StringProperty('')
    dTempHi0 = StringProperty('')
    dTempLo0 = StringProperty('')
    dTime1 = StringProperty('')
    dIcon1 = StringProperty('')
    dTempHi1 = StringProperty('')
    dTempLo1 = StringProperty('')
    dTime2 = StringProperty('')
    dIcon2 = StringProperty('')
    dTempHi2 = StringProperty('')
    dTempLo2 = StringProperty('')
    dTime3 = StringProperty('')
    dIcon3 = StringProperty('')
    dTempHi3 = StringProperty('')
    dTempLo3 = StringProperty('')
    dTime4 = StringProperty('')
    dIcon4 = StringProperty('')
    dTempHi4 = StringProperty('')
    dTempLo4 = StringProperty('')
    dTime5 = StringProperty('')
    dIcon5 = StringProperty('')
    dTempHi5 = StringProperty('')
    dTempLo5 = StringProperty('')
    dTime6 = StringProperty('')
    dIcon6 = StringProperty('')
    dTempHi6 = StringProperty('')
    dTempLo6 = StringProperty('')

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
        self.cTime = (datetime.utcfromtimestamp(self.fcast.cTime).strftime('%A, %b %d'))
        self.cTemp = str(int(self.fcast.cTemp))
        self.cIcon = str(self.fcast.cIcon)
        self.cSummary = "Today is "+(str(self.fcast.cSummary).lower())
        self.cHumidity = str(int(self.fcast.cHumidity*100))
        self.cUVIndex = self.UvLvl[int(self.fcast.cUVIndex)]
        self.cOzone = str(self.fcast.cOzone)
        self.cWindSpeed = str(self.fcast.cWindSpeed)
        self.cWindGust = str(self.fcast.cWindGust)
        self.cVisibility = self.VisLvl[int(self.fcast.cVisi)]

        self.dTime0 = datetime.utcfromtimestamp(self.fcast.dList()[0].time).strftime('%a')
        self.dIcon0 = str(self.fcast.dList()[0].icon)
        self.dTempHi0 = str(int(self.fcast.dList()[0].temperatureHigh))
        self.dTempLo0 = str(int(self.fcast.dList()[0].temperatureLow))
        self.dTime1 = datetime.utcfromtimestamp(self.fcast.dList()[1].time).strftime('%a')
        self.dIcon1 = str(self.fcast.dList()[1].icon)
        self.dTempHi1 = str(int(self.fcast.dList()[1].temperatureHigh))
        self.dTempLo1 = str(int(self.fcast.dList()[1].temperatureLow))
        self.dTime2 = datetime.utcfromtimestamp(self.fcast.dList()[2].time).strftime('%a')
        self.dIcon2 = str(self.fcast.dList()[2].icon)
        self.dTempHi2 = str(int(self.fcast.dList()[2].temperatureHigh))
        self.dTempLo2 = str(int(self.fcast.dList()[2].temperatureLow))
        self.dTime3 = datetime.utcfromtimestamp(self.fcast.dList()[3].time).strftime('%a')
        self.dIcon3 = str(self.fcast.dList()[3].icon)
        self.dTempHi3 = str(int(self.fcast.dList()[3].temperatureHigh))
        self.dTempLo3 = str(int(self.fcast.dList()[3].temperatureLow))
        self.dTime4 = datetime.utcfromtimestamp(self.fcast.dList()[4].time).strftime('%a')
        self.dIcon4 = str(self.fcast.dList()[4].icon)
        self.dTempHi4 = str(int(self.fcast.dList()[4].temperatureHigh))
        self.dTempLo4 = str(int(self.fcast.dList()[4].temperatureLow))
        self.dTime5 = datetime.utcfromtimestamp(self.fcast.dList()[5].time).strftime('%a')
        self.dIcon5 = str(self.fcast.dList()[5].icon)
        self.dTempHi5 = str(int(self.fcast.dList()[5].temperatureHigh))
        self.dTempLo5 = str(int(self.fcast.dList()[5].temperatureLow))
        self.dTime6 = datetime.utcfromtimestamp(self.fcast.dList()[6].time).strftime('%a')
        self.dIcon6 = str(self.fcast.dList()[6].icon)
        self.dTempHi6 = str(int(self.fcast.dList()[6].temperatureHigh))
        self.dTempLo6 = str(int(self.fcast.dList()[6].temperatureLow))




googleKey = 'key'
darkSkyKey = 'key'
googleAPICaller = GoogleAPICaller(googleKey)
darkSkyAPICaller = DarkSkyAPICaller(darkSkyKey)
sm=Builder.load_file('weather.kv')
class WeatherApp(App):#app class must match kv file minus "app"
    #screen_manager = ObjectProperty()
    def build(self):#pass the instance of the class to the function so it knows it parent.
        self.icon='data/icon.png'
        Window.bind(on_keyboard=self.on_key)
        return sm

    def on_key(self, window, key, *args):
        if key == 27:  # the esc key
            if sm.current_screen.name == "SearchScreen":
                return False  # exit the app from this page
            elif sm.current_screen.name == "ForecastScreen":
                sm.current = "SearchScreen"
                sm.transition.direction = 'right'
                return True

if __name__ == "__main__":#only autorun the code if the file is being run as main.
    WeatherApp().run()



