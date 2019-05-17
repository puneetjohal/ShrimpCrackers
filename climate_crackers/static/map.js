// Generating map from locationIQ API
var API_KEY = "pk.738f40deb14792dababc73f9349b0bfd";

// var latitude = parseFloat(40.7128)
// var longitude = parseFloat(-74.0060)

var URL = "https://maps.locationiq.com/v2/staticmap?key="+API_KEY+"&markers=icon:large-blue-cutout|"+latitude+","+longitude

// console.log(URL);
var map = document.getElementById("map");
var img = document.createElement("img");
img.setAttribute("src",URL);
// console.log(img);
map.append(img);

