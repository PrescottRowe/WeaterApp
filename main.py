#__version__ = "1.4"
#This file and the sister weather.kv files were written by Precott Rowe
#forecast.py, google.py, and darkskyapi.py were written by Fredson Laguna
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



class ForecastScreen(Screen):#This is the scrreen that shows all of the weather data
    def __init__(self, **kwargs):
        super(ForecastScreen, self).__init__(**kwargs)
        self.drop_down = Drop_Down()#the drop down list is used for the menu history tab to view past
        #searches that have been stored ofline in a json file

    #These dictionaries are used to turn the forcast raitings into something more understandable
    UvLvl = {0:"Very Low", 1:"Very Low", 2:"Low", 3:"Low", 4:"Normal", 5:"Normal", 6:"High",
             7:"Very High", 8:"Damaging", 9:"Dangerous", 10:"Dangerous"}
    VisLvl = {10:"Very High", 9:"High", 8:"Good", 7:"Okay", 6:"Sub-par", 5:"Bad", 4:"Bad",
              3:"Terrible", 2:"Terrible", 1:"Dangerous", 0:"Dangerous" }

    #variables for dynamic storage
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

    #The offline storage can be cleared if the user does a swipe motion on the history button
    def wipe_data(self):
        #The kivy docs said that it was safer to delete one by one like this because
        #the clear() fuunction is  being phased out for something else
        entry_list = WeatherApp.store.keys()
        entry_count = WeatherApp.store.count()
        for i in range(0, entry_count):
            WeatherApp.store.store_delete(entry_list[i])

    #This fuunction pulls data from the internal storage .json file
    def get_data(self, address):
        self.address = address#need to reset address so menu bar can update when looking at history
        #c is for current (right now) stats
        self.cTime = WeatherApp.store.get(address)['cTime']
        self.cTemp = WeatherApp.store.get(address)['cTemp']
        self.cIcon = WeatherApp.store.get(address)['cIcon']#icon is a string that specifes the png file to pull
        self.cSummary = WeatherApp.store.get(address)['cSummary']
        self.cHumidity = WeatherApp.store.get(address)['cHumidity']
        self.cUVIndex = self.UvLvl[int(float(WeatherApp.store.get(address)['cUVIndex']))]#cast from float to int is safer for python 2.7
        #the casting is to match the values to dictionary keys
        self.cOzone = WeatherApp.store.get(address)['cOzone']
        self.cWindSpeed = WeatherApp.store.get(address)['cWindSpeed']
        self.cWindGust = WeatherApp.store.get(address)['cWindGust']
        self.cVisibility = self.VisLvl[int(float(WeatherApp.store.get(address)['cVisibility']))]

        #d is daily stats for the 7day forecast
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

#set data is the core of the program that checks the address with google and then saves to a json file
    def set_data(self):
        isAddressLegit=False
        while isAddressLegit == False:#used to avoid doing weather searches on gibberish strings
            googleAPICaller.setJsonData(self.label_location)
            isAddressLegit = googleAPICaller.checkIfValidAddress()
            if isAddressLegit == True:
                predictionList = googleAPICaller.predictLocation(self.label_location)
                address = predictionList[0]#if an unkown address is forced then it will take its best guess
                googleAPICaller.setJsonData(address)
                googleAPICaller.setAddress()

        #The darksky api uses geo cords so we used the google api to get the geo cords for
        #a location and then send them to darksky
        latitude = googleAPICaller.getLatitude()
        longitude = googleAPICaller.getLongitude()
        forecastData = darkSkyAPICaller.getForecastJsonData(latitude, longitude)
        formattedAddress = googleAPICaller.getFormattedAddress()

        #The link to the organized back end data that holds many fetures for ease of future development
        self.fcast = Forecast(forecastData, formattedAddress)
        self.address = str(self.fcast.address)

        #this is the main push of data to the internal storage
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

        # add the key to history so we can look up the saved data
        self.addToHistory()

    #when a user clicks a saved city this function updates the weather to reflect the change
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

    #function to create history dropdown menu
    def addToHistory(self):
        self.drop_down.clear_widgets()#clear is used to let this function double as a refresher
        entry_list= WeatherApp.store.keys()#list all of the stored locations
        entry_count=WeatherApp.store.count()#number of cities
        #makes a drop down button for each city in the json file
        for i in range (0,entry_count):
            #this is the button being made
            btn = Button(text=entry_list[i], size_hint_y=None, height=self.height/15)
            #this is binding the button to pass the name of the city to the setter function when selected
            btn.bind(on_release=lambda btn: self.drop_down.select(btn.text))
            #adding the button to the tree
            self.drop_down.add_widget(btn)
            self.drop_down.bind(on_select=lambda instance, x: self.get_data(x))

class Drop_Down(DropDown):
    pass#used as an abstract dropdown class

#This is the first screen that you come too
class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.drop_down = Drop_Down()

    location = StringProperty('No location')
    F=ForecastScreen()#object to make screen management easier

    def predict_location(self,address):
        self.drop_down.clear_widgets()#clear is used to refresh
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

                    if i<2:#originaly there were 5 predictions showing. i have it at one because it looks better
                        #but i left it as a mutatable to easily change the drop down number if i want to later
                        btn=Button(text=location, size_hint_y=None, height=self.height/15)
                        #add and bind the button to be even driven
                        btn.bind(on_release=lambda btn: self.drop_down.select(btn.text))
                        self.drop_down.add_widget(btn)
                        self.drop_down.bind(on_select=lambda instance, x: self.set_location(x))#for some reason either the api or the api caller
                        #makes me need a terminating character otherwise it cuts off the last letter and can produce random results. need to ask fred to check up on this

    #basically just a screen changing function for once everything looks good to go
    def set_location(self, address):
        self.location = str(address)
        self.manager.current = "ForecastScreen"
        sm.transition.direction = 'left'

#KEYS
googleKey = 'AIzaSyAO-zV0XBi8hM0pnAtLDdoSVtmhWrl8JWM'
darkSkyKey = '4a05668b390431d4f52a20934a3f67ac'

googleAPICaller = GoogleAPICaller(googleKey)
darkSkyAPICaller = DarkSkyAPICaller(darkSkyKey)
#screen manager object
sm=Builder.load_file('weather.kv')


class WeatherApp(App):#app class must match kv file minus "app"
    #opens the json file for data storage in app directory
    store = JsonStore('weather.json')
    def build(self):#pass the instance of the class to the function so it knows it parent.
        self.icon='data/icon.png'
        #this is the keyboard bind for the android buttons
        Window.bind(on_keyboard=self.on_key)
        return sm
    #all 3 android buttons work and a double back exits which i am told is a standard thing to do on android
    def on_key(self, window, key, *args):
        if key == 27:  # the esc key
            if sm.current_screen.name == "SearchScreen":
                return False  # exit the app from this page
            elif sm.current_screen.name == "ForecastScreen":
                sm.current = "SearchScreen"
                sm.transition.direction = 'right' #natural looking transisitons
                return True


if __name__ == "__main__":#only autorun the code if the file is being run as main.
    WeatherApp().run()




