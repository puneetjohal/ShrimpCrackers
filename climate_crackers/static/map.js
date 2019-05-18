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

var loc = document.getElementById("location").innerHTML;

var form = document.getElementsByTagName("form")[1];
var info = [loc, latitude, longitude];
var names = ["loc", "lat", "long"];


for(var i = 0; i<3; i++) {
  var new_ele = document.createElement("input");
  new_ele.setAttribute("type","hidden");
  new_ele.setAttribute("name",names[i]);
  new_ele.setAttribute("value", info[i]);
  // console.log(new_ele);
  form.append(new_ele);
  // console.log(form);
}

