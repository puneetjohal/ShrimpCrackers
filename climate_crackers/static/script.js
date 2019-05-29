var svg = d3.select("#landing_map");

var path = d3.geoPath();

var fill = d3.scaleLog()
    .domain([10, 500])
    .range(["brown", "steelblue"]);
  //.interpolator(d3.interpolateCool);

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
      .style("fill", function(d) { return fill(path.area(d)); })
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

var slider = document.getElementById("year")
var display = document.getElementById("current_year")
display.innerHTML = slider.value;
slider.oninput = function() {
  display.innerHTML = this.value;
}
