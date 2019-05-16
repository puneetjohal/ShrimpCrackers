import json
import urllib.request

token = {"token": "jggiGITnyOHqgrVCGTgWCMycNLzIchHJ"}
#url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-02"
'''
url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/datasets/"
req = urllib.request.Request(url, data=None, headers={"token": "jggiGITnyOHqgrVCGTgWCMycNLzIchHJ"})
response = urllib.request.urlopen(req)
data = json.loads(response.read())

for x in range(0, len(data['results'])):
    print(data['results'][x]['id'])
    print(data['results'][x]['name'])
'''

url = "http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GSOY&locationid=ZIP:28801&startdate=2000-04-01&enddate=2010-04-01&datatypeid=EMNT&limit=100"
req = urllib.request.Request(url, data=None, headers=token)
response = urllib.request.urlopen(req)
data = json.loads(response.read())

print(data['results'])
