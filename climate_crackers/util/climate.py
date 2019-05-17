import json
import urllib.request

token = {"token": "jggiGITnyOHqgrVCGTgWCMycNLzIchHJ"}

def getcityid(city, state):
    offset = 0
    for x in range(0,10):
        url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&limit=1000&offset=" + str(offset)
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        for x in range(0, len(data['results'])):
            if city in data['results'][x]['name'] and state in data['results'][x]['name']:
                print(data['results'][x]['id'])
                return data['results'][x]['id']
        offset += 1000
    print("NOT FOUND")
    return "NOT FOUND"

def getInfo(city, state):
    ID = getcityid(city, state)
    if ID == "NOT FOUND":
        return "NOT FOUND"
    url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOM&locationid="+ ID +"&startdate=2009-04-01&enddate=2010-04-01&datatypeid=EMNT&limit=100"
    req = urllib.request.Request(url, data=None, headers=token)
    response = urllib.request.urlopen(req)
    data = json.loads(response.read())
    print(data['results'])
    return data['results']

getInfo("Los Angeles", "CA")

'''
GET DATASETS
url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/datasets/"
req = urllib.request.Request(url, data=None, headers={"token": "jggiGITnyOHqgrVCGTgWCMycNLzIchHJ"})
response = urllib.request.urlopen(req)
data = json.loads(response.read())

for x in range(0, len(data['results'])):
    print(data['results'][x]['id'])
    print(data['results'][x]['name'])
'''
'''
GSOM SAMPLE QUERY
url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOM&locationid=FIPS:01017&startdate=2009-04-01&enddate=2010-04-01&datatypeid=EMNT&limit=100"
req = urllib.request.Request(url, data=None, headers=token)
response = urllib.request.urlopen(req)
data = json.loads(response.read())

print(data['results'])
'''
'''
GET COUNTIES
url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CNTY"
req = urllib.request.Request(url, data=None, headers=token)
response = urllib.request.urlopen(req)
data = json.loads(response.read())

print(data['results'])
'''
'''
GET LOCATION CATEGORIES
url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locationcategories?limit=1000"
req = urllib.request.Request(url, data=None, headers=token)
response = urllib.request.urlopen(req)
data = json.loads(response.read())

print(data['results'])
'''
