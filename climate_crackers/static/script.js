var svg = d3.select("#landing_map");

var path = d3.geoPath();

var fill = d3.scaleLog()
    .domain([10, 100])
    .range(["brown", "steelblue"]);
  //.interpolator(d3.interpolateCool);

var slider = document.getElementById("year")
var display = document.getElementById("current_year")
display.innerHTML = slider.value;
slider.oninput = function() {
  display.innerHTML = this.value;
}

var tavg = {};
//Loading average temperature data
d3.json("https://raw.githubusercontent.com/puneetjohal/ShrimpCrackers/master/climate_crackers/data/tavg.json", function(error, data) {
  if (error) throw error;

  for (county in data) {
    index = county.indexOf(" County");
    name = county.slice(0,index);
    counter = 1900;
    temps = [];
    for (obj in data[county]) {
      year = Object.keys(obj)[0];
      if (parseInt(year) != counter) {
        while (counter != parseInt(year)) {
          temps.push(0);
          counter = counter + 1;
        }
      }
      else {
        if (obj[year] === "") {
          val = 0;
        }
        else {
          val = parseInt(obj[year]);
        }
        temps.push(val);
      }
      counter = counter + 1;
    }
    while (counter < 2018) {
      temps.push(0);
      counter = counter + 1;
    }
    tavg[name] = temps;
  }
  console.log(tavg)
});

//Drawing US map
//JSON file being used here is an online version of the map.json file in the data directory. We aren't using the local version to bypass Chrome errors with opening a local file.
d3.json("https://cdn.jsdelivr.net/npm/us-atlas@2/us/10m.json", function(error, us) {
  if (error) throw error;

  svg.append("g")
      .attr("class", "counties")
    .selectAll("path")
    .data(topojson.feature(us, us.objects.counties).features)
    .enter().append("path")
      .attr("id", function(d) {
        return d.properties.name;
      })
      .attr("d", path)
      //.style("fill", function(d) { return fill(tavg[d.properties.name][parseInt(slider.value)-1900]); })
      .on("click", function(d) {
          console.log(this)
      });

  svg.append("path")
      .attr("class", "county-borders")
      .attr("d", path(topojson.mesh(us, us.objects.counties, function(a, b) { return a !== b; })));

  svg.append("g")
      .attr("class", "states")
    .selectAll("path")
    .data(topojson.feature(us, us.objects.states).features)
    .enter().append("path")
      .attr("d", path);

  svg.append("path")
      .attr("class", "state-borders")
      .attr("d", path(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; })));

});
