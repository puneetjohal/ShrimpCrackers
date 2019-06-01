# interacting with ipstack api
from flask import request
import urllib.request
import json

KEY = "505ea9a7b91d5ca93f52056ca5bf77fd"

def get_coord():
    IP = json.loads(urllib.request.urlopen("http://ip.jsontest.com/").read())['ip']
    URL = "http://api.ipstack.com/" + IP +"?access_key=" + KEY + "&output=json"
    req = urllib.request.Request(URL)
    response = urllib.request.urlopen(req)
    data = json.loads(response.read())
    return data
