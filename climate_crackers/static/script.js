var svg = d3.select("#landing_map");
var placeholder = d3.select("#loading")

var w = 320, h = 50;

var path = d3.geoPath();

var key = d3.select("#legend");
key.style("padding-top", "20px")
  .style("height", "80px");

var legend = key.append("defs")
      .append("svg:linearGradient")
      .attr("id", "gradient")
      .attr("x1", "0%")
      .attr("y1", "100%")
      .attr("x2", "100%")
      .attr("y2", "100%")
      .attr("spreadMethod", "pad");

legend.append("stop")
  .attr("offset", "0%")
  .attr("stop-color", "steelblue")
  .attr("stop-opacity", 1);

// legend.append("stop")
//   .attr("offset", "33%")
//   .attr("stop-color", "#bae4bc=")
//   .attr("stop-opacity", 1);
//
// legend.append("stop")
//   .attr("offset", "66%")
//   .attr("stop-color", "#7bccc4")
//   .attr("stop-opacity", 1);

legend.append("stop")
  .attr("offset", "100%")
  .attr("stop-color", "red")
  .attr("stop-opacity", 1);

key.append("rect")
  .attr("width", w - 20)
  .attr("height", h - 30)
  .style("fill", "url(#gradient)")
  .attr("transform", "translate(10,10)");

var y = d3.scaleLinear()
  .range([310, 10])
  .domain([100, 0]);

var yAxis = d3.axisBottom()
  .scale(y)
  .ticks(5);

key.append("g")
  .attr("class", "y axis")
  .attr("transform", "translate(0,30)")
  .call(yAxis);



//Loading average temperature data

//Drawing US map
//JSON file being used here is an online version of the map.json file in the data directory. We aren't using the local version to bypass Chrome errors with opening a local file.
d3.json("https://cdn.jsdelivr.net/npm/us-atlas@2/us/10m.json", function(error, us) {
  if (error) throw error;

  svg.append("g")
      .attr("class", "counties")
    .selectAll("path")
    .data(topojson.feature(us, us.objects.counties).features)
    .enter().append("path")
      .attr("class", "county-path")
      .attr("id", function(d) {
        return d.properties.name;
      })
      .attr("d", path)
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

//Loading average temperature data
d3.json("https://raw.githubusercontent.com/puneetjohal/ShrimpCrackers/master/climate_crackers/data/newLandingData.json", function(error, data) {
  if (error) throw error;

  //Color interpolation
  var fill = d3.scaleLinear()
      .domain([15, 100])
      .range(["steelblue", "red"]);
    //.interpolator(d3.interpolateCool);

  //Year display on HTML
  var slider = document.getElementById("year")
  var display = document.getElementById("current_year")
  display.innerHTML = slider.value;
  slider.oninput = function() {
    display.innerHTML = this.value;
    update(this.value);
  }

  //Color change when slider is adjusted
  d3.select("#year").on("input", function() {
    update(+this.value);
  });
  function update(value) {
    svg.selectAll(".county-path") //PROBLEM OCCURS HERE
      .style("fill", function(d) {
        // console.log(d3.select(this));
        // console.log(d);
        temp = getTemp(d.properties.name, value);
        if (temp == 0) {
          return "#D3D3D3";
        }
        else {
        return fill(temp);
        }
      });
  }
  //Helper that get the tavg from temps object
  function getTemp(name, year) {
    var temp;
    // console.log(data[year])
    // for (var i=0; i < data[year].length; i++) {
    //   // console.log(data[year][i]);
    //   curCounty = data[year][i]["county"];
    //   index = curCounty.indexOf(" County");
    //   adjName = curCounty.slice(0,index);
    //   if (adjName === name) {
    //     temp = data[year][i]["TAVG"];
    //     break;
    //   }
    // }
    name = name + " County";

    temp = data[year][name];

    if (temp == undefined || temp.toString() === "" || temp.toString() === "0") {
      return 0;
    }

    else {
        // console.log(temp);
        return parseFloat(temp);
    }
  }

  update(2010);
  placeholder.remove();
}); //Close temps JSON
