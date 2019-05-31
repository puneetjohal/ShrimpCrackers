import json
import urllib.request
import time

token = {"token": "jggiGITnyOHqgrVCGTgWCMycNLzIchHJ"}

#===============================================================================
# COUNTY/CITY WEATHER INFORMATION FOR SEARCH FUNCTION
#===============================================================================

def getcitylist():
    '''Return a dictionary of available cities in the format of "city":"id".'''
    offset = 0
    ret_dict = {}
    for x in range(0,2):#total: 1988 cities
        url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&limit=1000&offset=" + str(offset)
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        for each in data['results']:
            ret_dict[each['name']] = each['id']
        offset += 1000
    return ret_dict

city_list = getcitylist()
# print(len(city_list))

def getcityid(city, state):
    print("getting city id for", city)
    for key in city_list.keys():
        if city in key and state in key:
            return city_list[key]
    return "NOT FOUND"

# print(getcityid("Salt Lake City", "UT"))
# print(getcityid("Brooklyn", "NY"))

def getcountylist():
    offset = 0
    ret_dict = {}
    for x in range(0, 4):#total: 3,179 counties
        url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CNTY&limit=1000&offset=" + str(offset)
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        for each in data['results']:
            ret_dict[each['name']] = each['id']
        offset += 1000
    return ret_dict

county_list = getcountylist()
# print(len(county_list))

def getcountyid(county, state):
    print("getting county id for", county)
    for key in county_list.keys():
        if county in key and state in key:
            return county_list[key]
    return "NOT FOUND"

# print(getcountyid("Kings County", "NY"))

def getSearchInfo(city, county, state):
    if city == "":
        ID = "NOT FOUND"
    else:
        ID = getcityid(city, state)
    if ID == "NOT FOUND" and county != "":
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
    cntyIDs = [4,000]
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

def getStations():
    with open('cntyIDs.json') as json_file:
        cntyIDs = json.load(json_file)
    info = []
    for x in range(0, 1000):
        #get the stations
        stations = ""
        print(cntyIDs[x][0])
        '''
        url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datatypeid=TAVG&locationid=" +cntyIDs[x]
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
        '''
    with open('stations.json', 'w') as outfile:
        json.dump(info, outfile)

# getStations()

def getCntyInfo():
    with open('stations.json') as json_file:
        stations = json.load(json_file)
    info = {}
    for x in stations:
        #get the info
        url = "https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-summary-of-the-year&dataTypes=TAVG&stations=" + stations[x] + "&startDate=1900-01-01&endDate=2018-12-31&format=json&units=standard"
        req = urllib.request.Request(url, data=None, headers=token)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        alist = []
        for j in range(0, len(data)):
            if 'TAVG' in data[j]:
                alist.append({data[j]['DATE']:data[j]['TAVG']})
            else:
                alist.append({data[j]['DATE']: ""})
        info[x] = alist
    with open('tavg.json', 'w') as outfile:
        json.dump(info, outfile)

#getCntyInfo()
