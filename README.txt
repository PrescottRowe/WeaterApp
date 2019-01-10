# WeatherApp
12/12/18
API's : Google(to get location cordinates based off of zip/city), Darksky(to get forecast data worldwide)

Completed app, slow and buggy but i will now stop development on this. It was more for learning python than for actual use. Although it does work and stores weather data localy in a small json file to minimize api calls if you re-search the same location within a day or two. 

Last update:
+truncated the float numbers
+fixed icon spacing for different sized screens
+android back button and home button both work now
+added a menu bar,search,history button
+search screen button along with search on_enter
+more py3->py2 errors fixed and found //since apk builder didnt work with py3
+unix time is now more readable
+more text markup
+logo splash screen
+better screen transitions
+faster search button
+tinted background image for easier readablility of text
+high and low temps in weekly
+Visibility and Uv index are now phrases(high,low, etc) instead of 1-10 integers
+Day forecast summary is now a phrase rather than the api word that is returned
+save history, dropdown list and link
+has offline storage
+click a day to view more
+default load icons
+search suggestions
+request data before loading pictures to speed up total load

