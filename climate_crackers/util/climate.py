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


#===============================================================================
# COUNTY WEATHER INFORMATION FOR LANDING PAGE
#===============================================================================
def getCountyID():
    '''
    returns a dictionary
    keys: name of county
    value: county id
    '''
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

def getCntyStations():
    '''
    returns a dictionary
    keys: name of the county
    value: string of the station ids that support TAVG
    '''
    CntyStations = {}
    cntyIDs = getCountyID()
    for x in cntyIDs:
        stations = ""
        url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datatypeid=TAVG&locationid=" +cntyIDs[x]
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        for i in range(0, len(data['results'])):
            stations = stations + data['results'][i]['id'] + ","
        #remove trailing comma
        stations = stations[:-1]
        print(stations)
        CntyStations[x] = stations
        time.sleep(.05)
    return CntyStations
        
def getCountyInfo():
    CntyStations = getCntyStations()
    for c in CntyStations:
        info = []
        url = "https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-summary-of-the-year&dataTypes=TAVG&stations=" + CntyStations[c] + "&startDate=1900-01-01&endDate=2018-12-31&format=json&units=standard"
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        print(data)
        

getCountyInfo()
