// Generating map from locationIQ API
// var apidata = JSON.parse(data);
// var API_KEY = apidata["token"];
// console.log(API_KEY);
var API_KEY = "pk.738f40deb14792dababc73f9349b0bfd";

// var latitude = parseFloat(40.7128)
// var longitude = parseFloat(-74.0060)

var URL = "https://maps.locationiq.com/v2/staticmap?key="+API_KEY+"&zoom=12&markers=icon:large-blue-cutout|"+latitude+","+longitude

// console.log(URL);
var map = document.getElementById("map");
var img = document.createElement("img");
img.setAttribute("src",URL);
img.setAttribute("width", "450px");
img.setAttribute("height", "400px");
// console.log(img);
map.append(img);

// var loc = document.getElementById("location").innerHTML;

// var form = document.getElementsByTagName("form")[0];
// // console.log(form);
// var info = [loc, latitude, longitude];
// var names = ["city", "lat", "long"];
//
//
// for(var i = 0; i<3; i++) {
//   var new_ele = document.createElement("input");
//   new_ele.setAttribute("type","hidden");
//   new_ele.setAttribute("name",names[i]);
//   new_ele.setAttribute("value", info[i]);
//   // console.log(new_ele);
//   form.append(new_ele);
//   // console.log(form);
// }
