document.addEventListener('DOMContentLoaded', () => {
  // Handle form submission
  document.getElementById('fetch-button').addEventListener('click', async () => {
    const authors = $('#authors-dropdown').val(); // Get selected values
    const works = $('#works-dropdown').val(); // Get selected values
    const hops = document.getElementById('hops').value;
    const exclude_list = $('#exclude-list-dropdown').val(); // Get selected values

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

      // Wire up renderGraph here
      renderGraph(data.graph);

    } catch (error) {
      console.error('Error generating graph:', error);

      // Optionally render mock data for testing
      const mockData = {
        nodes: [
          { id: 'A', label: 'Node A', type: 'author' },
          { id: 'B', label: 'Node B', type: 'work' }
        ],
        edges: [
          { source: 'A', target: 'B' }
        ]
      };
      renderGraph(mockData);
    }
  });
});

function renderGraph(graph) {
  const svg = d3.select('svg');
  svg.selectAll('*').remove(); // Clear previous graph

  const width = +svg.attr('width');
  const height = +svg.attr('height');

  const graphGroup = svg.append('g'); // Attach all elements to this group

  const zoom = d3.zoom()
    .scaleExtent([0.5, 3])
    .on('zoom', (event) => {
      graphGroup.attr('transform', event.transform);
    });

  svg.call(zoom);

  const simulation = d3.forceSimulation(graph.nodes)
    .force('link', d3.forceLink(graph.edges).id(d => d.id).distance(100))
    .force('charge', d3.forceManyBody().strength(-50))
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
    .attr('class', d => `node ${d.type}`) // Apply specific class based on node type
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

  // Add labels to graphGroup
  const labels = graphGroup.append('g')
    .selectAll('text')
    .data(graph.nodes)
    .join('text')
    .attr('class', 'label')
    .attr('dy', -15) // Position labels slightly above nodes
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

    // Update label positions to match nodes
    labels
      .attr('x', d => d.x)
      .attr('y', d => d.y);

  });

  // Add optional zoom controls for debugging
  d3.select('body').append('div')
    .style('position', 'fixed')
    .style('bottom', '10px')
    .style('right', '10px')
    .html(`
      <button id="zoomIn">Zoom In</button>
      <button id="zoomOut">Zoom Out</button>
    `);

  d3.select('#zoomIn').on('click', () => svg.transition().call(zoom.scaleBy, 1.2));
  d3.select('#zoomOut').on('click', () => svg.transition().call(zoom.scaleBy, 0.8));

}
