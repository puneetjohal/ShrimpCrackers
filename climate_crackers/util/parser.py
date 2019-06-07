#File used to reformat tavg.json to be compatible with landing page
import os
import json

DIR = os.path.dirname(__file__) or '.'
DIR += '/../'

editted = {}

with open(DIR + "data/tavg.json", "r") as input:
    data = json.load(input)
    for county in data.keys():
        index = county.index(" County")
        name = county[:index]
        counter = 1900
        temps = []
        for obj in data[county]: # [ {obj}, {"year":"temp"}, {} ]
            year = list(obj.keys())[0]
            if int(year) != counter:
                while counter != int(year):
                    temps.append(0)
                    counter = counter + 1
            else:
                if obj[year] == "":
                    val = 0
                else:
                    val = int(obj[year])
                temps.append(val)
            counter = counter + 1
        while counter < 2018:
            temps.append(0)
            counter = counter + 1
        editted[name] = temps

with open(DIR + "data/landingData.json", w) as output:
    #for chunk in json.JSONEncoder().iterencode(editted):
    #    output.write(chunk)
    json.dump(editted, output)
