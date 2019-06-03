// precipitation bar graph
var GRAPH_W = 500;
var GRAPH_H = 300;
margin = {top: 50, right: 10, bottom: 30, left: 40};

// console.log(data);

data.forEach( d => {
    d["DATE"] = parseInt(d['DATE']);
    d['TAVG'] = parseFloat(d['TAVG']);
});

data.sort(function(a, b){
    return a.DATE - b.DATE;
});

p_data.forEach ( d => {
    d['DATE'] = parseInt(d['DATE']);
    d['PRCP'] = parseFloat(d['PRCP']);
});

p_data.sort(function(a,b){
    return a.DATE - b.DATE;
})

var p_graph = d3.select("#p_graph")
                .attr("width",GRAPH_W)
                .attr("height", GRAPH_H)

p_graph.append("rect")
  .attr("width", "100%")
  .attr("height", "100%")
  .attr("fill", "white");

x = d3.scaleTime()
  .domain([new Date(d3.min(p_data, d => d.DATE), 0, 1), new Date(d3.max(p_data, d => d.DATE), 0, 1)])
  .range([margin.left, GRAPH_W - margin.right]);

bar_x = d3.scaleBand()
  .domain(p_data.map(d => d.DATE))
  .range([margin.left, GRAPH_W - margin.right])
  .padding(0.1);

y = d3.scaleLinear()
  .domain([0, d3.max(p_data, d => d.PRCP)]).nice()
  .range([GRAPH_H - margin.bottom, margin.top]);

var color = d3.scaleOrdinal()
  .domain(p_data, d => d.DATE)
  .range(["#d6d6ea", "#9999cc"]);

xAxis = g => g
  .attr("transform", `translate(0,${GRAPH_H - margin.bottom})`)
  .call(d3.axisBottom(x).tickSizeOuter(0));

yAxis = g => g
  .attr("transform", `translate(${margin.left},0)`)
  .call(d3.axisLeft(y))
  .call(g => g.select(".domain").remove());

// console.log(p_graph);

p_graph.append("text")
  .attr("x", (GRAPH_W / 2))
  .attr("y", 0 + (margin.top / 2))
  .attr("text-anchor", "middle")
  .style("font-size", "16px")
  .style("text-decoration", "underline")
  .text("Precipitation vs Year");

var bar = p_graph.selectAll("g")
  .data(p_data)
  .enter()
  .append("g")
  .attr("fill", d => color(d.DATE));
  // .attr("transform", function (d, i) {
  //   return "translate(" + i * BAR_W + ", 0)"; });

p_graph.append("g")
  .call(xAxis);

p_graph.append("g")
  .call(yAxis);

bar.append("rect").attr("height", function (d) {
    return y(0) - y(d.PRCP);
  })
  .attr("width", bar_x.bandwidth())
  .attr("x", d => bar_x(d.DATE))
  .attr("y", d => y(d.PRCP));
// bar.append("text").attr("x", function (d){
//                                     return x(d.value) - 3;})
//                         .attr("y", barHeight / 2)
//                         .attr("dy", ".35em")
//                         .text(function(d) { return d.value; });

// =======================================================

var t_graph = d3.select("#t_graph")
                .attr("width",GRAPH_W)
                .attr("height", GRAPH_H)

t_graph.append("rect")
  .attr("width", "100%")
  .attr("height", "100%")
  .attr("fill", "white");

x = d3.scaleTime()
  .domain([new Date(d3.min(data, d => d.DATE), 0, 1), new Date(d3.max(data, d => d.DATE), 0, 1)])
  .range([margin.left, GRAPH_W - margin.right]);
  // .padding(0.1);

y = d3.scaleLinear()
  .domain([d3.min(data, d => d.TAVG) - 5, d3.max(data, d => d.TAVG)]).nice()
  .range([GRAPH_H - margin.bottom, margin.top]);

color = d3.scaleOrdinal()
  .domain(data, d => d.DATE.substring(2))
  .range(["#d6d6ea", "#9999cc"]);

line = d3.line()
  // .defined(d => !isNaN(d.TAVG))
  .x(d => x(new Date(d.DATE,0,1)))
  .y(d => y(d.TAVG));

// console.log(p_graph);

t_graph.append("text")
  .attr("x", (GRAPH_W / 2))
  .attr("y", 0 + (margin.top / 2))
  .attr("text-anchor", "middle")
  .style("font-size", "16px")
  .style("text-decoration", "underline")
  .text("Average Temperature vs Year");

t_graph.append("path")
  .datum(data)
  .attr("fill", "none")
  .attr("stroke", "steelblue")
  .attr("stroke-width", 1.5)
  .attr("stroke-linejoin", "round")
  .attr("stroke-linecap", "round")
  .attr("d", line);

// var t_bar = t_graph.selectAll("g")
//   .data(data)
//   .enter()
//   .append("g")
//   .attr("fill", d => color(d.DATE.substring(2)));

t_graph.append("g")
  .call(xAxis);

t_graph.append("g")
  .call(yAxis);

// t_bar.append("rect").attr("height", function (d) {
//     return y(0) - y(parseFloat(d.TAVG));
//   })
//   .attr("width", x.bandwidth())
//   .attr("x", d => x(d.DATE.substring(2)))
//   .attr("y", d => y(parseFloat(d.TAVG)));
