import { refreshDropdowns } from './dropdown.js';

document.addEventListener('DOMContentLoaded', async () => {
    // Check if initialization parameters are provided by the backend
    const initialParams = window.initialParams || null;

    if (initialParams) {
        // Populate dropdowns and inputs
        const authorsDropdown = $('#authors-dropdown');
        const worksDropdown = $('#works-dropdown');
        const excludeDropdown = $('#exclude-list-dropdown');

        if (initialParams.authors.length > 0) {
          await fetchLabelsAndPopulateDropdown(initialParams.authors, authorsDropdown);
        }
        if (initialParams.works.length > 0) {
          await fetchLabelsAndPopulateDropdown(initialParams.works, worksDropdown);
        }
        if (initialParams.exclude_list.length > 0) {
          await fetchLabelsAndPopulateDropdown(initialParams.exclude_list, excludeDropdown);
        }

        // Set hops value
        document.getElementById('hops').value = initialParams.hops;

        // Fetch and render the graph immediately
        const payload = {
          authors: initialParams.authors,
          works: initialParams.works,
          hops: parseInt(initialParams.hops, 10),
          exclude_list: initialParams.exclude_list
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
          renderGraph(data.graph); // Render the graph from POST response
        } catch (error) {
          console.error('Error generating graph:', error);
        }
    }


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

      renderGraph(data.graph); // Render the graph from POST response
    } catch (error) {
      console.error('Error generating graph:', error);
    }
  });

});

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

  svg.call(zoom);

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
    .attr('class', d => `node ${d.type}`)
    .attr('r', d => {
      if (d.is_central) return 17;
      if (d.is_excluded) return 15;
      return 10;
    })
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
      }))
    .on('contextmenu', (event, d) => {
    // Prevent default browser context menu
    event.preventDefault();

    // Create or show a custom context menu
    let menu = d3.select('.custom-context-menu');
    if (menu.empty()) {
        menu = d3.select('body').append('div')
            .attr('class', 'custom-context-menu')
            .style('position', 'absolute')
            .style('background', '#fff')
            .style('padding', '8px')
            .style('border', '1px solid #ccc')
            .style('border-radius', '4px')
            .style('box-shadow', '0 4px 8px rgba(0, 0, 0, 0.1)')
            .style('display', 'none');
    }

    // Type-to-path mapping for Open Link
    const typeMapping = { author: "person", work: "work" };
    const entityPath = typeMapping[d.type] || d.type;

    // Populate the menu
    menu.html(`
        <a href="https://www.panditproject.org/entity/${d.id}/${entityPath}" target="_blank" style="display:block; margin-bottom: 5px;">View in Pandit</a>
        <br>
        <div style="margin-bottom: 10px;">
            <label for="hops-input" style="display:inline-block; width: 50px; text-align: right; margin-right: 5px; color: black;">Hops:</label>
            <input type="number" id="hops-input" value="2" style="width: 50px;">
        </div>
        <button id="recenter-btn" style="display:block;">Recenter Graph</button>
        <br>
        <!-- New material: Exclude Node option -->
        <button id="exclude-node-btn" style="display:block; margin-top: 5px;">Collapse Node</button>
    `);

    // Position and show the menu
    menu.style('left', `${event.pageX}px`)
        .style('top', `${event.pageY}px`)
        .style('display', 'block');

    menu.on('click', (e) => e.stopPropagation()); // Prevent menu clicks from propagating

    // Update the recenter button handler to stop propagation
    document.getElementById('recenter-btn').onclick = async (e) => {
        e.stopPropagation(); // Prevent the button click from closing the menu
        const hops = document.getElementById('hops-input').value;

        const payload = {
            authors: d.type === 'author' ? [d.id] : [],
            works: d.type === 'work' ? [d.id] : [],
            hops: parseInt(hops, 10),
            exclude_list: [] // Add exclusions if needed
        };

        // Fetch and re-render the graph
        try {
            const response = await fetch('/api/graph/subgraph', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const newGraph = await response.json();
            renderGraph(newGraph.graph);

            // Update dropdowns with the new center only
            const authorsDropdown = $('#authors-dropdown');
            const worksDropdown = $('#works-dropdown');

            await refreshDropdowns(authorsDropdown, worksDropdown);

            // Redo dropdown for the specific type
            if (d.type === 'author') {
                authorsDropdown.append(new Option(d.label, d.id, true, true)); // Add new center
                authorsDropdown.trigger('change'); // Refresh Select2
            } else if (d.type === 'work') {
                worksDropdown.append(new Option(d.label, d.id, true, true)); // Add new center
                worksDropdown.trigger('change'); // Refresh Select2
            }

            // Update hops input to match the current value
            document.getElementById('hops').value = hops;
        } catch (error) {
            console.error('Error recentering graph:', error);
        }

        // Hide the menu
        menu.style('display', 'none');
    };

    // Exclude Node button handler
    document.getElementById('exclude-node-btn').onclick = async (e) => {
        e.stopPropagation(); // Prevent the button click from closing the menu

        // Add the selected node to the exclude list
        const exclude_list = $('#exclude-list-dropdown').val();
        if (!exclude_list.includes(d.id)) {
            exclude_list.push(d.id);
        }

        // Update the dropdown and trigger Select2 change event
        $('#exclude-list-dropdown').val(exclude_list).trigger('change');

        const authors = $('#authors-dropdown').val();
        const works = $('#works-dropdown').val();
        const hops = parseInt(document.getElementById('hops').value, 10);

        const payload = {
            authors: authors,
            works: works,
            hops: hops,
            exclude_list: exclude_list
        };

        // Fetch and re-render the graph
        try {
            const response = await fetch('/api/graph/subgraph', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const updatedGraph = await response.json();
            renderGraph(updatedGraph.graph);
        } catch (error) {
            console.error('Error excluding node:', error);
        }

        // Hide the menu
        menu.style('display', 'none');
    };
  });

  // Hide menu on outside click
  d3.select('body').on('click', (event) => {
    d3.select('.custom-context-menu').style('display', 'none');
  });

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
}

//  // Add zoom controls
//  const zoomControls = d3.select('body').append('div')
//    .style('position', 'fixed')
//    .style('bottom', '10px')
//    .style('right', '10px')
//    .html(`
//      <button id="zoomIn">Zoom In</button>
//      <button id="zoomOut">Zoom Out</button>
//    `);
//
//  // Attach zoom functions to buttons
//  d3.select('#zoomIn').on('click', () => svg.transition().call(zoom.scaleBy, 1.2));
//  d3.select('#zoomOut').on('click', () => svg.transition().call(zoom.scaleBy, 0.8));
//}