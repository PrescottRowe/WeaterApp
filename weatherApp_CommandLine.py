from googleAPI import GoogleAPICaller
from darkskyAPI import DarkSkyAPICaller

def main():
    address = input("Enter address information: ")
    print("\n")


    googleKey = 'super duper key'
    darkSkyKey = 'other super duper key'
    
    googleAPICaller = GoogleAPICaller(googleKey)
    darkSkyAPICaller = DarkSkyAPICaller(darkSkyKey) 
    googleAPICaller.setAddress(address)

    latitude = googleAPICaller.getLatitude()
    longitude = googleAPICaller.getLongitude()
    weeklyForecast = darkSkyAPICaller.getForecastJsonData(latitude, longitude)
    darkSkyAPICaller.setCurrentForecast(weeklyForecast)
    darkSkyAPICaller.setWeeklyForecast(weeklyForecast)

    googleAPICaller.printAddress_Long_Lat()
    print()
    darkSkyAPICaller.printWeeklyForecast()
    
    

if __name__ == '__main__': main()

