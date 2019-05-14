import json
import urllib.request

KEY = "AeQXeELfNwZglxceETnnOASZGit7hoW1"
#VALID LOCATION: 1600+Pennsylvania+Ave+NW,Washington,DC,20500
geocode = "http://open.mapquestapi.com/geocoding/v1/address?key=" + KEY + "&location="

#MAPQUEST API
#get longitude and latitude of a given city from user's search
def getOptions(city):
    response = urllib.request.urlopen(geocode+city)
    options = json.loads(response.read())
    results = options['results'][0]['locations']
    print(results)
    for x in range(0, len(results))
    
getOptions("Brooklyn")
