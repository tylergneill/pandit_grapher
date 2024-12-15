document.addEventListener('DOMContentLoaded', async () => {
  try {
    // Fetch dropdown options from the backend
    const response = await fetch('/api/graph/dropdown-options');
    if (!response.ok) throw new Error('Failed to fetch dropdown options');

    const options = await response.json();

    // Populate dropdowns with options
    const centerDropdown = document.getElementById('subgraph_center');
    const blacklistDropdown = document.getElementById('blacklist');

    options.forEach(option => {
      const opt = document.createElement('option');
      opt.value = option.id;
      opt.textContent = option.label;
      centerDropdown.appendChild(opt.cloneNode(true)); // Clone for reuse
      blacklistDropdown.appendChild(opt);
    });

    // Initialize Select2 AFTER populating options
    $('#subgraph_center').select2({
      placeholder: 'Select Subgraph Center',
      allowClear: true
    });

    $('#blacklist').select2({
      placeholder: 'Select Blacklist',
      allowClear: true
    });

    // Handle form submission
    document.getElementById('fetch-button').addEventListener('click', async () => {
      const subgraphCenter = $('#subgraph_center').val(); // Get selected values
      const hops = document.getElementById('hops').value;
      const blacklist = $('#blacklist').val(); // Get selected values

      const payload = {
        subgraph_center: subgraphCenter,
        hops: parseInt(hops, 10),
        blacklist: blacklist
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

        // Call your graph rendering logic here
      } catch (error) {
        console.error('Error generating graph:', error);
      }
    });
  } catch (error) {
    console.error('Error loading dropdown options:', error);
  }
});
