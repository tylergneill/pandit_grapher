document.getElementById('fetch-button').addEventListener('click', async () => {
  const subgraphCenter = document.getElementById('subgraph_center').value.split(',').map(x => x.trim());
  const hops = parseInt(document.getElementById('hops').value, 10);
  const blacklist = document.getElementById('blacklist').value.split(',').map(x => x.trim());

  const parameters = {
    subgraph_center: subgraphCenter,
    hops: hops,
    blacklist: blacklist
  };

  // Display query parameters for debugging
  console.log('Query Parameters:', parameters);

  // Fetch graph data from the backend API
  const response = await fetch("http://127.0.0.1:5090/api/graph/subgraph", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(parameters)
  });

  if (!response.ok) {
    alert('Error fetching graph data. Please check your input.');
    return;
  }

  const data = await response.json();

  // Render the graph
  renderGraph(data.graph);
});

function renderGraph(graph) {
  const svg = d3.select('svg');
  svg.selectAll('*').remove(); // Clear the previous graph

  const width = +svg.attr('width');
  const height = +svg.attr('height');

  // Force simulation
  const simulation = d3.forceSimulation(graph.nodes)
    .force('link', d3.forceLink(graph.edges).id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-300))
    .force('center', d3.forceCenter(width / 2, height / 2));

  // Draw links
  const link = svg.append('g')
    .selectAll('line')
    .data(graph.edges)
    .join('line')
    .attr('class', 'link')
    .attr('stroke', '#999')
    .attr('stroke-opacity', 0.6);

  // Draw nodes
  const node = svg.append('g')
    .selectAll('circle')
    .data(graph.nodes)
    .join('circle')
    .attr('class', 'node')
    .attr('r', 10)
    .attr('fill', '#0074D9')
    .call(d3.drag()
      .on('start', event => {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
      })
      .on('drag', event => {
        event.subject.fx = event.x;
        event.subject.fy = event.y;
      })
      .on('end', event => {
        if (!event.active) simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
      }));

  // Add labels
  const labels = svg.append('g')
    .selectAll('text')
    .data(graph.nodes)
    .join('text')
    .attr('class', 'label')
    .attr('dy', -15)
    .attr('text-anchor', 'middle')
    .text(d => d.label);

  // Update positions dynamically
  simulation.on('tick', () => {
    link
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y);

    node
      .attr('cx', d => d.x)
      .attr('cy', d => d.y);

    labels
      .attr('x', d => d.x)
      .attr('y', d => d.y);
  });
}
