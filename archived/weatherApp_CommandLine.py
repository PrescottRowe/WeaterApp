from googleAPI import GoogleAPICaller
from darkskyAPI import DarkSkyAPICaller
from forecast import Forecast

def main():
    #googleKey = 'super duper key'
    #darkSkyKey = 'other super duper key'
    googleKey = 'key'
    darkSkyKey = 'key'
    googleAPICaller = GoogleAPICaller(googleKey)
    darkSkyAPICaller = DarkSkyAPICaller(darkSkyKey)     


    isAddressLegit = False

    while isAddressLegit == False:
        address = input("Enter address information: ")
        print("\n")

        googleAPICaller.setJsonData(address)
        isAddressLegit = googleAPICaller.checkIfValidAddress()
        if isAddressLegit == True:
            predictionList = googleAPICaller.predictLocation(address)
            if len(predictionList) > 1:
                print("Multiple locations have been found:")
                i = 0
                for location in predictionList:
                    print(str(i) + ')', location)
                    i = i + 1
                selection = input("Choose a location: ")
                address = predictionList[int(selection)]
                googleAPICaller.setJsonData(address)
                googleAPICaller.setAddress()
        
           
    latitude = googleAPICaller.getLatitude()
    longitude = googleAPICaller.getLongitude()
    forecastData = darkSkyAPICaller.getForecastJsonData(latitude, longitude)
    formattedAddress = googleAPICaller.getFormattedAddress()
    
    fcast = Forecast(forecastData, formattedAddress)
    print("Address: ", fcast.address)
    print("long: ", fcast.long, "lat: ",  fcast.lat)
    print("Timezone: ", fcast.timezone)

    # the following is just a quick and sloppy way of printing all the classes' attributes
    # the only thing that should be accessed are the @property attributes and never the _private ones
    print()
    for k, v in vars(fcast._fAlerts).items():
        print(k,'=',v)
        
    
    print()
    print("*******************Current Forecast*******************") 
    for k, v in vars(fcast._fCurrent).items():
        print(k,'=',v)

    # not every location searched will have a minutely forecast for some reason, which will cause this to crash
    # if minutely forecasts are to be added in the mobile version, there needs to be a check if the class has no instance attributes
    print()
    print("*******************Minutely Forecast*******************")
    print(fcast.mSummary)
    print(fcast.mIcon)    
    for data in (fcast._fMinutely._minutelyList):
        for k,v in vars(data).items():
            print(k,'=',v)
        print()


    print()
    print("*******************Hourly Forecast*******************")
    print(fcast.hSummary)
    print(fcast.hIcon)
    for data in (fcast.hList()):
        for k,v in vars(data).items():
            print(k, '=', v)
        print()

    print()
    print("*******************Daily Forecast*******************")
    print(fcast.dSummary)
    print(fcast.dIcon)
    for data in (fcast.dList()):
        for k,v in vars(data).items():
            print(k, '=', v)
        print()

    
if __name__ == '__main__': main()

