# interacting with locationIQ API
import urllib.request

API_KEY = "pk.738f40deb14792dababc73f9349b0bfd"


def gen_map(latitude, longitude):
    URL = "https://maps.locationiq.com/v2/staticmap?key="+API_KEY+"&markers=icon:large-blue-cutout|"+str(latitude)+","+str(longitude)
    r = urllib.request.urlopen(req)
    print (r)

gen_map(40.7128,-74.0060)
