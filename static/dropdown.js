document.addEventListener('DOMContentLoaded', async () => {
  try {
    // Fetch dropdown options from the backend
    const response = await fetch('/api/graph/all-entities');
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
  } catch (error) {
    console.error('Error loading dropdown options:', error);
  }
});
