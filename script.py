##requires install of geopy
import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="app")
location = geolocator.geocode("Tampa, FL")##enter city into parentheses
location = str(location)
location = location.split(",")##splits information into city, state, county, country
##requires city, state format e.g. Tampa, FL, so data may need formatting
city = location[0]
county = location[1]
state = location[2]
#country = location[3]
#print(location)
print(county)
