import json
import urllib.request
import time

token = {"token": "jggiGITnyOHqgrVCGTgWCMycNLzIchHJ"}

def getcityid(city, state):
    offset = 0
    for x in range(0,2):#total: 1988 cities
        url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&limit=1000&offset=" + str(offset)
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        print(len(data['results']))
        for x in range(0, len(data['results'])):
            if city in data['results'][x]['name'] and state in data['results'][x]['name']:
                print(data['results'][x]['id'])
                return data['results'][x]['id']
        offset += 1000
    print("NOT FOUND")
    return "NOT FOUND"

#getcityid("Fort Myers", "TX")

def getInfoCity(city, state):
    ID = getcityid(city, state)
    if ID == "NOT FOUND":
        return "NOT FOUND"
    url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOM&locationid="+ ID +"&startdate=2009-04-01&enddate=2010-04-01&datatypeid=TAVG&limit=100"
    req = urllib.request.Request(url, data=None, headers=token)
    response = urllib.request.urlopen(req)
    data = json.loads(response.read())
    print(data['results'])
    return data['results']

#getInfoCity("Los Angeles", "CA")

def getCountyID():
    cntyIDs = {}
    offset = 0
    for x in range(0, 4):#total: 3,179 counties
        url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CNTY&limit=1000&offset=" + str(offset)
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        print(len(data['results']))
        for i in range(0, len(data['results'])):
            cntyIDs[data['results'][i]['name']] = data['results'][i]['id']
        offset += 1000
    return cntyIDs

def getCountyInfo():
    cntyIDs = getCountyID()
    tavgInfo = {}
    for x in cntyIDs:
        info = []
        tavgInfo[x] = info
        url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&locationid=" +cntyIDs[x] + "&startdate=2001-01-01&enddate=2010-01-01&limit=1000"
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        for i in range(0, data['results']):
            print(data['results'][0]['date'])
            print(data['results'][0]['value'])
        time.sleep(1)
        
getCountyInfo()


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
