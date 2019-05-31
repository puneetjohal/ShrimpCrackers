import json
import urllib.request
import time

token = {"token": "jggiGITnyOHqgrVCGTgWCMycNLzIchHJ"}

#===============================================================================
# COUNTY/CITY WEATHER INFORMATION FOR SEARCH FUNCTION
#===============================================================================

def getcityid(city, state):
    print("getting city id")
    offset = 0
    for x in range(0,2):#total: 1988 cities
        url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&limit=1000&offset=" + str(offset)
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        # print(len(data['results']))
        for x in range(0, len(data['results'])):
            # print(data['results'][x]['name'])
            if city in data['results'][x]['name'] and state in data['results'][x]['name']:
                print(data['results'][x]['id'])
                return data['results'][x]['id']
        offset += 1000
    # print("NOT FOUND")
    return "NOT FOUND"

# getcityid("Fort Myers", "TX")
# getcityid("Salt Lake City", "UT")
# print(getcityid("Brooklyn", "NY"))

def getcountyid(county, state):
    print("getting county id")
    offset = 0
    for x in range(0, 4):#total: 3,179 counties
        url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CNTY&limit=1000&offset=" + str(offset)
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        # print(len(data['results']))
        for i in range(0, len(data['results'])):
            # print(data['results'][x]['name'])
            # if state in data['results'][i]['name']:
            #     print(data['results'][i]['name'])
            if county in data['results'][i]['name'] and state in data['results'][i]['name']:
                print(data['results'][i]['id'])
                return data['results'][i]['id']
        offset += 1000
    print("NOT FOUND")
    return "NOT FOUND"

def getSearchInfo(city, county, state):
    ID = getcityid(city, state)
    if ID == "NOT FOUND":
        ID = getcountyid(county, state)
    stations = ""
    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datatypeid=TAVG&locationid=" + ID
    req = urllib.request.Request(url, data=None, headers=token)
    response = urllib.request.urlopen(req)
    data = json.loads(response.read())
    for i in range(0, len(data['results'])):
        s = data['results'][i]['id']
        #remove the colon and everything before it
        s = s.split(':', 1)[-1]
        stations += s + ","
    #remove trailing comma
    stations = stations[:-1]
    # print(stations)
    url = "https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-summary-of-the-year&dataTypes=TAVG&stations=" + stations + "&startDate=1900-01-01&endDate=2018-12-31&format=json&units=standard"
    req = urllib.request.Request(url, data=None, headers=token)
    response = urllib.request.urlopen(req)
    data = json.loads(response.read())
    ret_data = []
    for entry in data:
        if 'TAVG' in entry:
            ret_data.append(entry)
    return ret_data

# print(getSearchInfo("New York City", "Kings County", "NY"))
#===============================================================================
# COUNTY WEATHER INFORMATION FOR LANDING PAGE
#===============================================================================
def getCountyID():
    '''
    returns a dictionary
    keys: name of county
    value: county id
    '''
    cntyIDs = []
    offset = 0
    for x in range(0, 4):#total: 3,179 counties
        url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CNTY&limit=1000&offset=" + str(offset)
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        print(len(data['results']))
        for i in range(0, len(data['results'])):
            cntyIDs.append([data['results'][i]['name'], data['results'][i]['id']])
        offset += 1000
    with open('cntyIDs.json', 'w') as outfile:
        json.dump(cntyIDs, outfile)

#getCountyID()

def getStations(lbound, ubound):
    info = []
    with open('cntyIDs.json') as json_file:
        cntyIDs = json.load(json_file)
    if ubound == 4000:
        ubound = len(cntyIDs)
    print(ubound)
    for x in range(lbound, ubound):
        print(x)
        #get the stations
        stations = ""
        url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datatypeid=TAVG&locationid=" +cntyIDs[x][1]
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        if 'results' in data:
            for i in range(0, len(data['results'])):
                s = data['results'][i]['id']
                #remove the colon and everything before it
                s = s.split(':', 1)[-1]
                stations += s + ","
            #remove trailing comma
            stations = stations[:-1]
            info.append([cntyIDs[x][0],stations])
            time.sleep(1)
    with open('stations.json', 'a') as stationfile:
        json.dump(info, stationfile)

#getStations(0, 1000) ALREADY RAN THIS
#getStations(1000, 2000) ALREADY RAN THIS
#getStations(2000, 3000) ALREADY RAN THIS
getStations(3000, 4000)


def getCntyInfo(batch):
    with open('stations.json') as json_file:
        stations = json.load(json_file)
    info = {}
    for x in range(0, len(stations[batch])):
        #get the info
        print(stations[batch][x][1])
        url = "https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-summary-of-the-year&dataTypes=TAVG&stations=" + stations[batch][x][1] + "&startDate=1900-01-01&endDate=2018-12-31&format=json&units=standard"
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        alist = []
        for j in range(0, len(data)):
            if 'TAVG' in data[j]:
                alist.append({data[j]['DATE']:data[j]['TAVG']})
            else:
                alist.append({data[j]['DATE']: ""})
        info[stations[batch][x][0]] = alist
    with open('tavg.json', 'w') as outfile:
        json.dump(info, outfile)

#getCntyInfo(0)
#getCntyInfo(1)
#getCntyInfo(2)
#getCntyInfo(3)
