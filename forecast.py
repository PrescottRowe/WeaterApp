class Forecast:
    def __init__(self, forecastJsonData, formattedAddress):
        self._timezone = forecastJsonData['timezone']              # (eg: America/New York)
        self._latitude = forecastJsonData['latitude']
        self._longitude = forecastJsonData['longitude']
        self._formattedAddress = formattedAddress
        
        self._fCurrent = Forecast_Currently(forecastJsonData)
        self._fMinutely = Forecast_Minutely(forecastJsonData)
        self._fHourly = Forecast_Hourly(forecastJsonData)
        self._fDaily = Forecast_Daily(forecastJsonData)

        self._fAlerts = Alerts(forecastJsonData)

    @property
    def timezone(self):
        return self._timezone
    @property
    def lat(self):
        return self._latitude
    @property
    def long(self):
        return self._longitude
    @property
    def address(self):
        return self._formattedAddress


    #***** The below properties are used for retrieving data from the class "Forecast_Currently" *****#
    @property
    def cTime(self):
        return self._fCurrent._time # returns the unix time, refer to http://strftime.org/ for converting from unix time to human readable time
    @property
    def cSummary(self):
        return self._fCurrent._summary        
    @property
    def cIcon(self):
        return self._fCurrent._icon
    @property
    def cTemp(self):
        return self._fCurrent._temperature
    @property
    def cATemp(self):
        return self._fCurrent._apparentTemperature
    @property
    def cDewPoint(self):
        return self._fCurrent._dewPoint
    @property
    def cHumidity(self):
        return self._fCurrent._humidity
    @property
    def cPressure(self):
        return self._fCurrent._pressure
    @property
    def cWindSpeed(self):
        return self._fCurrent._windSpeed
    @property
    def cWindGust(self):
        return self._fCurrent._windGust
    @property
    def cWindBearing(self):
        return self._fCurrent._windBearing
    @property
    def cNearestStormBearing(self):
        return self._fCurrent._nearestStormBearing
    @property
    def cNearestStormDistance(self):
        return self._fCurrent._nearestStormDistance
    @property
    def cUVIndex(self):
        return self._fCurrent._uvIndex
    @property
    def cVisi(self):
        return self._fCurrent._visibility
    @property
    def cOzone(self):
        return self._fCurrent._ozone
    

    #***** The below properties are used for retrieving data from the class "Forecast_Minutely" *****#
    @property
    def mSummary(self):
        return self._fMinutely._summary
    @property
    def mIcon(self):
        return self._fMinutely._icon
    @property
    def mList(self):
        return self._fMinutely._minutelyList # returns the list of minute-by-minute forecasts
    

    #***** The below properties are used for retrieving data from the class "Forecast_Hourly" *****#
    @property
    def hSummary(self):
        return self._fHourly._summary
    def hIcon(self):
        return self._fHourly._icon
    def hList(self):
        return self._fHourly._hourlyList

    #***** The below properties are used for retrieving data from the class "Forecast_Daily" *****#
    @property
    def dSummary(self):
        return self._fDaily._summary
    def dIcon(self):
        return self._fDaily._icon
    def dList(self):
        return self._fDaily._dailyList
    


# class that contains current/in the moment weather conditions
class Forecast_Currently:
    def __init__(self, forecastJsonData):
        c = forecastJsonData['currently']
        self._time = c['time']        			# unix time
        self._summary = c['summary']   			# e.g. "Mostly Cloudy"
        self._icon = c['icon']      			# icon for the weather
        self._temperature = c['temperature']          	# average temperature
        self._apparentTemperature = c['apparentTemperature']  	# what the temperature feels like
        self._dewPoint = c['dewPoint']                  # the dew point in degrees Fahrenheit.
        self._humidity = c['humidity']
        self._pressure = c['pressure']                  # the sea-level air pressure in millibars.
        self._windSpeed = c['windSpeed']                #The wind speed in miles per hour.
        self._windGust = c.get('windGust', '')          #The wind gust speed in miles per hour.
        self._windBearing = c.get('windBearing', '')
        self._nearestStormBearing = c.get('nearestStormBearing', '')    #The approximate direction of the nearest storm in degrees, with true north at 0° and progressing clockwise. (If nearestStormDistance is zero, then this value will not be defined.)
        self._nearestStormDistance = c.get('nearestStormDistance', '')  #The approximate distance to the nearest storm in miles. (A storm distance of 0 doesn’t necessarily refer to a storm at the requested location, but rather a storm in the vicinity of that location.)
        self._uvIndex = c['uvIndex']
        self._visibility = c['visibility']              # the average visibility in miles, capped at 10 mile
        self._ozone = c['ozone']                        # the columnar density of total atmospheric ozone at the given time in Dobson units.
        
        
# class that contains 61 minutely forecasts for the next hour within a list
# I've noticed that the minutely forecast data is only present during rainy weather. It is often not present on the darksky site
class Forecast_Minutely:
    def __init__(self, forecastJsonData):
        if 'minutely' in forecastJsonData:
            m = forecastJsonData['minutely']
            self._summary = m['summary']
            self._icon = m['icon']
            self._minutelyList = list()         # list that will store instances of class Minutely, there should be 61 minutely forecasts stored
            for data in m['data']:
                self._minutelyList.append(Minutely(data['time'], data.get('precipIntensity', ''), data.get('precipProbability', ''), data.get('precipIntensityError', ''), data.get('precipType', '') ))
            
        

# contains by-the-minute forecast 
class Minutely:
    def __init__(self, time, precipIntensity, precipProbability, precipIntensityError,  precipType):
        self._time = time
        self._precipIntensity = precipIntensity
        self._precipProbability = precipProbability
        self._precipIntensityError = precipIntensityError
        self._precipType = precipType

    @property
    def time(self):
        return self._time
    @property
    def precipIntensity(self):
        return self._precipIntensity
    @property
    def precipIntensityError(self):
        return self._precipIntensityError
    @property
    def precipType(self):
        return self._precipType
            

#contains by-the-hour forecast for the next two days within a list
class Forecast_Hourly:
    def __init__(self, forecastJsonData):
        h = forecastJsonData['hourly']
        self._summary = h['summary']
        self._icon = h['icon']
        self._hourlyList = list()
        for data in h['data']:
            self._hourlyList.append(Hourly(data['time'], data['summary'], data['icon'], data.get('precipIntensity', ''), data.get('precipProbability', ''), data['temperature'], data['apparentTemperature'], data['dewPoint'], data['humidity'], data['pressure'], data['windSpeed'], data['windGust'], data.get('windBearing', ''), data['cloudCover'], data['uvIndex'], data['visibility'], data['ozone'] ))

#contains by-the-hour forecast
class Hourly:
    def __init__(self, time, summary, icon, precipIntensity, precipProbability, temperature, apparentTemperature, dewPoint, humidity, pressure, windSpeed, windGust, windBearing, cloudCover, uvIndex, visibility, ozone):
        self._time = time
        self._summary = summary
        self._icon = icon
        self._precipIntensity = precipIntensity
        self._precipProbability = precipProbability
        self._temperature = temperature
        self._apparentTemperature = apparentTemperature
        self._dewPoint = dewPoint
        self._humidity = humidity
        self._pressure = pressure
        self._windSpeed = windSpeed
        self._windGust = windGust
        self._windBearing = windBearing
        self._cloudCover = cloudCover
        self._uvIndex = uvIndex
        self._visibility = uvIndex
        self._ozone = ozone

    @property
    def time(self):
        return _time
    @property
    def summary(self):
        return _summary
    @property
    def icon(self):
        return _icon
    @property
    def precipIntensity(self):
        return _precipIntensity
    @property
    def precipProbability(self):
        return _precipProbability
    @property
    def temperature(self):
        return _temperature
    @property
    def apparentTemperature(self):
        return _apparentTemperature
    @property
    def dewPoint(self):
        return _dewPoint
    @property
    def humidity(self):
        return _humidity
    @property
    def pressure(self):
        return _pressure
    @property
    def windSpeed(self):
        return _windSpeed
    @property
    def windGust(self):
        return _windGust
    @property
    def windBearing(self):
        return _windBearing
    @property
    def cloudCover(self):
        return _cloudCover
    @property
    def uvIndex(self):
        return _uvIndex
    @property
    def visibility(self):
        return _visibility
    @property
    def ozone(self):
        return _ozone        

class Forecast_Daily:
    def __init__(self, forecastJsonData):
        d = forecastJsonData['daily']
        self._summary = d['summary']
        self._icon = d['icon']
        self._dailyList = list()
        for data in d['data']:
            self._dailyList.append( Daily(data['time'], data['summary'], data['icon'], data['sunriseTime'], data['sunsetTime'], data['moonPhase'], data.get('precipIntensity',''), data.get('precipIntensityMax',''), data.get('precipIntensityMaxTime',''), data.get('precipProbability',''), data.get('precipType',''), data['temperatureHigh'], data['temperatureHighTime'], data['temperatureLow'], data['temperatureLowTime'], data['apparentTemperatureHigh'], data['apparentTemperatureHighTime'], data['apparentTemperatureLow'], data['apparentTemperatureLowTime'], data['dewPoint'], data['humidity'], data['pressure'], data['windSpeed'], data['windGust'], data['windGustTime'], data.get('windBearing',''), data['cloudCover'], data['uvIndex'], data['uvIndexTime'], data['visibility'], data['ozone'] ))

class Daily:
    def __init__(self,time,summary,icon,sunriseTime,sunsetTime,moonPhase,precipIntensity,precipIntensityMax,precipIntensityMaxTime,precipProbability,precipType,temperatureHigh,temperatureHighTime,temperatureLow,temperatureLowTime,apparentTemperatureHigh,apparentTemperatureHighTime,apparentTemperatureLow,apparentTemperatureLowTime,dewPoint,humidity,pressure,windSpeed,windGust,windGustTime,windBearing,cloudCover,uvIndex,uvIndexTime,visibility,ozone):
        self._time = time
        self._summary = summary
        self._icon = icon
        self._sunriseTime = sunriseTime
        self._sunsetTime = sunsetTime
        self._moonPhase = moonPhase
        self._precipIntensity = precipIntensity
        self._precipIntensityMax = precipIntensityMax
        self._precipIntensityMaxTime = precipIntensityMaxTime
        self._precipProbability = precipProbability
        self._precipType = precipType
        self._temperatureHigh = temperatureHigh
        self._temperatureHighTime = temperatureHighTime
        self._temperatureLow = temperatureLow
        self._temperatureLowTime = temperatureLowTime
        self._apparentTemperatureHigh = apparentTemperatureHigh
        self._apparentTemperatureHighTime = apparentTemperatureHighTime
        self._apparentTemperatureLow = apparentTemperatureLow
        self._apparentTemperatureLowTime = apparentTemperatureLowTime
        self._dewPoint = dewPoint
        self._humidity = humidity
        self._pressure = pressure
        self._windSpeed = windSpeed
        self._windGust = windGust
        self._windGustTime = windGustTime
        self._windBearing = windBearing
        self._cloudCover = cloudCover
        self._uvIndex = uvIndex
        self._uvIndexTime = uvIndexTime
        self._visibility = visibility
        self._ozone = ozone

    @property
    def time(self):
        return _time
    @property
    def summary(self):
        return _summary
    @property
    def icon(self):
        return _icon
    @property
    def sunriseTime(self):
        return _sunriseTime
    @property
    def sunsetTime(self):
        return _sunsetTime
    @property
    def moonPhase(self):
        return _moonPhase
    @property
    def precipIntensity(self):
        return _precipIntensity
    @property
    def precipIntensityMax(self):
        return _precipIntensityMax
    @property
    def precipIntensityMaxTime(self):
        return _precipIntensityMaxTime
    @property
    def precipProbability(self):
        return _precipProbability
    @property
    def precipType(self):
        return _precipType
    @property
    def temperatureHigh(self):
        return _temperatureHigh
    @property
    def temperatureHighTime(self):
        return _temperatureHighTime
    @property
    def temperatureLow(self):
        return _temperatureLow
    @property
    def temperatureLowTime(self):
        return _temperatureLowTime
    @property
    def apparentTemperatureHigh(self):
        return _apparentTemperatureHigh
    @property
    def apparentTemperatureHighTime(self):
        return _apparentTemperatureHighTime
    @property
    def apparentTemperatureLow(self):
        return _apparentTemperatureLow
    @property
    def apparentTemperatureLowTime(self):
        return _apparentTemperatureLowTime
    @property
    def dewPoint(self):
        return _dewPoint
    @property
    def humidity(self):
        return _humidity
    @property
    def pressure(self):
        return _pressure
    @property
    def windSpeed(self):
        return _windSpeed
    @property
    def windGust(self):
        return _windGust
    @property
    def windGustTime(self):
        return _windGustTime
    @property
    def windBearing(self):
        return _windBearing
    @property
    def cloudCover(self):
        return _cloudCover
    @property
    def uvIndex(self):
        return _uvIndex
    @property
    def uvIndexTime(self):
        return _uvIndexTime
    @property
    def visibility(self):
        return _visibility
    @property
    def ozone(self):
        return _ozone
        

class Alerts:
    def __init__(self, forecastJsonData):
        if 'alerts' in forecastJsonData:
            a = forecastJsonData['alerts'][0]
            self._title = a.get('title', '')
            self._time = a.get('time','')
            self._expires = a.get('expires','')
            self._description = a.get('description','')
            self._uri = a.get('uri','')

        
                 
