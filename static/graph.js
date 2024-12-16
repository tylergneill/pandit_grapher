document.addEventListener('DOMContentLoaded', () => {
  // Handle form submission for generating graphs
  document.getElementById('fetch-button').addEventListener('click', async () => {
    const authors = $('#authors-dropdown').val(); // Get selected authors
    const works = $('#works-dropdown').val(); // Get selected works
    const hops = document.getElementById('hops').value; // Get hop count
    const exclude_list = $('#exclude-list-dropdown').val(); // Get exclusions

    const payload = {
      authors: authors,
      works: works,
      hops: parseInt(hops, 10),
      exclude_list: exclude_list
    };

    try {
      const response = await fetch('/api/graph/subgraph', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (!response.ok) throw new Error('Failed to generate graph');

      const data = await response.json();
      console.log('Graph data:', data);

      renderGraph(data.graph); // Render the graph from POST response
    } catch (error) {
      console.error('Error generating graph:', error);
    }
  });

  // Handle direct rendering via GET parameters
  const urlParams = new URLSearchParams(window.location.search);
  const works = urlParams.getAll('works'); // Fetch works list from URL
  const hops = urlParams.get('hops');

  if (works.length > 0 && hops) {
    const apiUrl = `/api/graph/render?${urlParams.toString()}`;
    fetchGraphData(apiUrl); // Fetch and render graph directly
  }
});

// Utility to fetch graph data from API for GET requests
async function fetchGraphData(apiUrl) {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) throw new Error('Failed to fetch graph data');

    const data = await response.json();
    console.log('Fetched graph data:', data);

    renderGraph(data); // Render the graph from GET response
  } catch (error) {
    console.error('Error fetching graph:', error);
  }
}

// Core function to render a graph using D3.js
function renderGraph(graph) {
  const svg = d3.select('svg');
  svg.selectAll('*').remove(); // Clear previous graph

  const width = +svg.attr('width');
  const height = +svg.attr('height');

  const graphGroup = svg.append('g'); // Group for all elements

  // Define zoom behavior
  const zoom = d3.zoom()
    .scaleExtent([0.5, 3])
    .on('zoom', (event) => graphGroup.attr('transform', event.transform));

  // Apply zoom behavior to the SVG element
  svg.call(zoom);

  // Simulation for force-directed graph
  const simulation = d3.forceSimulation(graph.nodes)
    .force('link', d3.forceLink(graph.edges).id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-100))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collide', d3.forceCollide(20));

  const link = graphGroup.append('g')
    .selectAll('line')
    .data(graph.edges)
    .join('line')
    .attr('class', 'link')
    .attr('stroke', '#999')
    .attr('stroke-opacity', 0.6);

  const node = graphGroup.append('g')
    .selectAll('circle')
    .data(graph.nodes)
    .join('circle')
    .attr('class', d => `node ${d.type}`) // Apply class based on type
    .attr('r', 10)
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

  const labels = graphGroup.append('g')
    .selectAll('text')
    .data(graph.nodes)
    .join('text')
    .attr('class', 'label')
    .attr('dy', -15)
    .attr('text-anchor', 'middle')
    .text(d => d.label);

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

  // Add zoom controls
  const zoomControls = d3.select('body').append('div')
    .style('position', 'fixed')
    .style('bottom', '10px')
    .style('right', '10px')
    .html(`
      <button id="zoomIn">Zoom In</button>
      <button id="zoomOut">Zoom Out</button>
    `);

  // Attach zoom functions to buttons
  d3.select('#zoomIn').on('click', () => svg.transition().call(zoom.scaleBy, 1.2));
  d3.select('#zoomOut').on('click', () => svg.transition().call(zoom.scaleBy, 0.8));
}
