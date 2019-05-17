import json
import urllib.request

KEY = "AeQXeELfNwZglxceETnnOASZGit7hoW1"
geocode = "http://open.mapquestapi.com/geocoding/v1/address?key=" + KEY + "&location="

#MAPQUEST API

'''
getOptions: given a location, gives a list of all areas including that string in the form of a list of lists
Each inner list has the location information and the associated latitude and longitude 
'''
def getOptions(city):
    response = urllib.request.urlopen(geocode+city)
    options = json.loads(response.read())
    results = options['results'][0]['locations']
    print(results)
    print(len(results))
    retlist = []
    for x in range(0, len(results)):
        alist = []
        alist.append(results[x]['adminArea6']) #neighborhood
        alist.append(results[x]['adminArea5']) #city
        alist.append(results[x]['adminArea4']) #county
        alist.append(results[x]['adminArea3']) #state
        alist.append(results[x]['adminArea1']) #country
        #alist.append(results[x]['latLng']['lat'])
        #alist.append(results[x]['latLng']['lng'])
        retlist.append(alist)
    print(retlist)
    return retlist
    
getOptions("Brooklyn")
