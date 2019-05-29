// precipitation bar graph
var GRAPH_W = 500;
var GRAPH_H = 300;
margin = {top: 50, right: 0, bottom: 30, left: 40};

var fake_data = [
  {
    name: "sophia",
    value: 123
  },
  {
    name: "tania",
    value: 456
  },
  {
    name: "puneet",
    value: 789
  },
  {
    name: "joyce",
    value: 345
  }];

var p_graph = d3.select("#p_graph")
                .attr("width",GRAPH_W)
                .attr("height", GRAPH_H)

p_graph.append("rect")
  .attr("width", "100%")
  .attr("height", "100%")
  .attr("fill", "white");

x = d3.scaleBand()
  .domain(fake_data.map(d => d.name))
  .range([margin.left, GRAPH_W - margin.right])
  .padding(0.1);

y = d3.scaleLinear()
  .domain([0, d3.max(fake_data, d => d.value)]).nice()
  .range([GRAPH_H - margin.bottom, margin.top]);

var color = d3.scaleOrdinal()
  .domain(fake_data, d => d.name)
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
  .data(fake_data)
  .enter()
  .append("g")
  .attr("fill", d => color(d.name));
  // .attr("transform", function (d, i) {
  //   return "translate(" + i * BAR_W + ", 0)"; });

p_graph.append("g")
  .call(xAxis);

p_graph.append("g")
  .call(yAxis);

bar.append("rect").attr("height", function (d) {
    return y(0) - y(d.value);
  })
  .attr("width", x.bandwidth())
  .attr("x", d => x(d.name))
  .attr("y", d => y(d.value));
// bar.append("text").attr("x", function (d){
//                                     return x(d.value) - 3;})
//                         .attr("y", barHeight / 2)
//                         .attr("dy", ".35em")
//                         .text(function(d) { return d.value; });
