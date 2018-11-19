# WeatherApp
11/15/18
API's : Google(to get location cordinates based off of zip/city), Darksky(to get forecast data worldwide)

Most of the gui is there, still need to add backend to make all of the buttons work along with various text markup changes.
notable changes since last version:


+truncated the float numbers
+fixed icon spacing for different sized screens
+android back button and home button both work now
+added a menu bar,search,history button
+search screen button along with search on_enter
+more py3->py2 errors fixed and found
+unix time is now readable
+more text markup
+logo splash screen
+better screen transitions
+search button
+tinted background image for easier readablility of text
+shows units
+high and low temps
+Visibility and Uv index are now phrases(high,low, etc) instead of 1-10 integers
+Day forecast summary is now a phrase rather than a word

Upcoming changes:
-click C or F option that is linked to unit types
-save history, dropdown list and link
-have offline storage
-side scrolling for weekly forcast
-click a day to view it
-default load icons
-search suggestions
-set data to load before pictures to speed up total load
-currently android keyboard selections append but should replace
