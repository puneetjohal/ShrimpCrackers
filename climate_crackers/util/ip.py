# interacting with ipstack api
from flask import request
import urllib.request
import json

KEY = "505ea9a7b91d5ca93f52056ca5bf77fd"

def get_coord():
    IP = request.remote_addr
    if IP == "127.0.0.1": # if running on local host
        req = urllib.request.Request("https://api.ipify.org?format=json")
        IP = json.loads(urllib.request.urlopen(req).read())['ip']
    # print(IP)
    URL = "http://api.ipstack.com/" + IP +"?access_key=" + KEY + "&output=json"
    req = urllib.request.Request(URL)
    response = urllib.request.urlopen(req)
    data = json.loads(response.read())
    return data
