#__version__ = "1.4"
import kivy
kivy.require('1.9.1')
from googleAPI import GoogleAPICaller
from darkskyAPI import DarkSkyAPICaller
from forecast import Forecast
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.storage.jsonstore import JsonStore
from datetime import datetime



class ForecastScreen(Screen):
    def __init__(self, **kwargs):
        super(ForecastScreen, self).__init__(**kwargs)
        self.drop_down = Drop_Down()

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

    def wipe_data(self):
        entry_list = WeatherApp.store.keys()
        entry_count = WeatherApp.store.count()
        for i in range(0, entry_count):
            WeatherApp.store.store_delete(entry_list[i])

    def get_data(self, address):
        self.address = address
        self.cTime = WeatherApp.store.get(address)['cTime']
        self.cTemp = WeatherApp.store.get(address)['cTemp']
        self.cIcon = WeatherApp.store.get(address)['cIcon']
        self.cSummary = WeatherApp.store.get(address)['cSummary']
        self.cHumidity = WeatherApp.store.get(address)['cHumidity']
        self.cUVIndex = self.UvLvl[int(float(WeatherApp.store.get(address)['cUVIndex']))]
        self.cOzone = WeatherApp.store.get(address)['cOzone']
        self.cWindSpeed = WeatherApp.store.get(address)['cWindSpeed']
        self.cWindGust = WeatherApp.store.get(address)['cWindGust']
        self.cVisibility = self.VisLvl[int(float(WeatherApp.store.get(address)['cVisibility']))]

        self.dTime0 = WeatherApp.store.get(address)['dTime0']
        self.dIcon0 = WeatherApp.store.get(address)['dIcon0']
        self.dTempHi0 = WeatherApp.store.get(address)['dTempHi0']
        self.dTempLo0 = WeatherApp.store.get(address)['dTempLo0']
        self.dTime1 = WeatherApp.store.get(address)['dTime1']
        self.dIcon1 = WeatherApp.store.get(address)['dIcon1']
        self.dTempHi1 = WeatherApp.store.get(address)['dTempHi1']
        self.dTempLo1 = WeatherApp.store.get(address)['dTempLo1']
        self.dTime2 = WeatherApp.store.get(address)['dTime2']
        self.dIcon2 = WeatherApp.store.get(address)['dIcon2']
        self.dTempHi2 = WeatherApp.store.get(address)['dTempHi2']
        self.dTempLo2 = WeatherApp.store.get(address)['dTempLo2']
        self.dTime3 = WeatherApp.store.get(address)['dTime3']
        self.dIcon3 = WeatherApp.store.get(address)['dIcon3']
        self.dTempHi3 = WeatherApp.store.get(address)['dTempHi3']
        self.dTempLo3 = WeatherApp.store.get(address)['dTempLo3']
        self.dTime4 = WeatherApp.store.get(address)['dTime4']
        self.dIcon4 = WeatherApp.store.get(address)['dIcon4']
        self.dTempHi4 = WeatherApp.store.get(address)['dTempHi4']
        self.dTempLo4 = WeatherApp.store.get(address)['dTempLo4']
        self.dTime5 = WeatherApp.store.get(address)['dTime5']
        self.dIcon5 = WeatherApp.store.get(address)['dIcon5']
        self.dTempHi5 = WeatherApp.store.get(address)['dTempHi5']
        self.dTempLo5 = WeatherApp.store.get(address)['dTempLo5']
        self.dTime6 = WeatherApp.store.get(address)['dTime6']
        self.dIcon6 = WeatherApp.store.get(address)['dIcon6']
        self.dTempHi6 = WeatherApp.store.get(address)['dTempHi6']
        self.dTempLo6 = WeatherApp.store.get(address)['dTempLo6']


    def set_data(self):
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

        WeatherApp.store.put(self.address, cTime = (datetime.utcfromtimestamp(self.fcast.cTime).strftime('%A, %b %d'))
            ,cTemp = str(int(self.fcast.cTemp))
            ,cIcon = str(self.fcast.cIcon)
            ,cSummary = str(datetime.utcfromtimestamp(self.fcast.cTime).strftime('%A'))+" is "+(str(self.fcast.cSummary).lower())
            ,cHumidity = str(int(self.fcast.cHumidity*100))
            ,cUVIndex = str(self.fcast.cUVIndex)
            ,cOzone = str(self.fcast.cOzone)
            ,cWindSpeed = str(self.fcast.cWindSpeed)
            ,cWindGust = str(self.fcast.cWindGust)
            ,cVisibility = str(self.fcast.cVisi)

            , dTime0 = datetime.utcfromtimestamp(self.fcast.dList()[0].time).strftime('%a')
            ,dIcon0 = str(self.fcast.dList()[0].icon)
            ,dTempHi0 = str(int(self.fcast.dList()[0].temperatureHigh))
            ,dTempLo0 = str(int(self.fcast.dList()[0].temperatureLow))
            ,dTime1 = datetime.utcfromtimestamp(self.fcast.dList()[1].time).strftime('%a')
            ,dIcon1 = str(self.fcast.dList()[1].icon)
            ,dTempHi1 = str(int(self.fcast.dList()[1].temperatureHigh))
            ,dTempLo1 = str(int(self.fcast.dList()[1].temperatureLow))
            ,dTime2 = datetime.utcfromtimestamp(self.fcast.dList()[2].time).strftime('%a')
            ,dIcon2 = str(self.fcast.dList()[2].icon)
            ,dTempHi2 = str(int(self.fcast.dList()[2].temperatureHigh))
            ,dTempLo2 = str(int(self.fcast.dList()[2].temperatureLow))
            ,dTime3 = datetime.utcfromtimestamp(self.fcast.dList()[3].time).strftime('%a')
            ,dIcon3 = str(self.fcast.dList()[3].icon)
            ,dTempHi3 = str(int(self.fcast.dList()[3].temperatureHigh))
            ,dTempLo3 = str(int(self.fcast.dList()[3].temperatureLow))
            ,dTime4 = datetime.utcfromtimestamp(self.fcast.dList()[4].time).strftime('%a')
            ,dIcon4 = str(self.fcast.dList()[4].icon)
            ,dTempHi4 = str(int(self.fcast.dList()[4].temperatureHigh))
            ,dTempLo4 = str(int(self.fcast.dList()[4].temperatureLow))
            ,dTime5 = datetime.utcfromtimestamp(self.fcast.dList()[5].time).strftime('%a')
            ,dIcon5 = str(self.fcast.dList()[5].icon)
            ,dTempHi5 = str(int(self.fcast.dList()[5].temperatureHigh))
            ,dTempLo5 = str(int(self.fcast.dList()[5].temperatureLow))
            ,dTime6 = datetime.utcfromtimestamp(self.fcast.dList()[6].time).strftime('%a')
            ,dIcon6 = str(self.fcast.dList()[6].icon)
            ,dTempHi6 = str(int(self.fcast.dList()[6].temperatureHigh))
            ,dTempLo6 = str(int(self.fcast.dList()[6].temperatureLow)))

        self.addToHistory()


    def switchDay(self,clickedDayNumber):

        self.cTime = (datetime.utcfromtimestamp(self.fcast.dList()[clickedDayNumber].time).strftime('%A, %b %d'))
        self.cTemp = str(int(self.fcast.dList()[clickedDayNumber].temperatureHigh))
        self.cIcon = str(self.fcast.dList()[clickedDayNumber].icon)
        self.cSummary = str(datetime.utcfromtimestamp(self.fcast.dList()[clickedDayNumber].time).strftime('%A'))+" is " + (str(self.fcast.dList()[clickedDayNumber].summary).lower())
        self.cHumidity = str(int(self.fcast.dList()[clickedDayNumber].humidity * 100))
        self.cUVIndex = self.UvLvl[int(self.fcast.dList()[clickedDayNumber].uvIndex)]
        self.cOzone = str(self.fcast.dList()[clickedDayNumber].ozone)
        self.cWindSpeed = str(self.fcast.dList()[clickedDayNumber].windSpeed)
        self.cWindGust = str(self.fcast.dList()[clickedDayNumber].windGust)
        self.cVisibility = self.VisLvl[int(self.fcast.dList()[clickedDayNumber].visibility)]

    def addToHistory(self):
        self.drop_down.clear_widgets()
        entry_list= WeatherApp.store.keys()
        entry_count=WeatherApp.store.count()
        for i in range (0,entry_count):
            btn = Button(text=entry_list[i], size_hint_y=None, height=self.height/15)
            btn.bind(on_release=lambda btn: self.drop_down.select(btn.text))
            self.drop_down.add_widget(btn)
            self.drop_down.bind(on_select=lambda instance, x: self.get_data(x))

class Drop_Down(DropDown):
    pass


class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)

    drop_down = Drop_Down()
    location = StringProperty('No location')
    F=ForecastScreen()

    def predict_location(self,address):
        self.drop_down.clear_widgets()
        if(address!="" and address!=" "):
            predictionList = googleAPICaller.predictLocation(address)
            if len(predictionList) > 1:
                #Multiple locations have been found
                i = 0

                for location in predictionList:
                    if(location.count(',')>3):#some google location will be something like
                        #"motel 6 ,north st, springfield, co, usa" so it gets rid of the building for the search.
                        temp=location.split(',',2)
                        location=temp[2]
                    i+=1

                    if i<2:
                        btn=Button(text=location, size_hint_y=None, height=self.height/15)
                        btn.bind(on_release=lambda btn: self.drop_down.select(btn.text))
                        self.drop_down.add_widget(btn)
                        self.drop_down.bind(on_select=lambda instance, x: self.set_location(x))#for some reason either the api or the api caller
                        #makes me need a terminating character otherwise it cuts off the last letter and can produce random results. need to ask fred to check up on this


    def set_location(self, address):
        self.location = str(address)
        #ForecastScreen.addToHistory(self.F)
        self.manager.current = "ForecastScreen"
        sm.transition.direction = 'left'


googleKey = 'key goes here'
darkSkyKey = 'key goes here'
googleAPICaller = GoogleAPICaller(googleKey)
darkSkyAPICaller = DarkSkyAPICaller(darkSkyKey)
sm=Builder.load_file('weather.kv')


class WeatherApp(App):#app class must match kv file minus "app"
    #screen_manager = ObjectProperty()
    store = JsonStore('weather.json')
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




