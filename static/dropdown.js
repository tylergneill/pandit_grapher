document.addEventListener('DOMContentLoaded', async () => {
  try {
    // Fetch dropdown options from the backend
    const response = await fetch('/api/graph/dropdown-options');
    if (!response.ok) throw new Error('Failed to fetch dropdown options');

    const options = await response.json();
    const centerDropdown = document.getElementById('subgraph_center');
    const blacklistDropdown = document.getElementById('blacklist');

    // Populate dropdowns with options
    options.forEach(option => {
      const opt = document.createElement('option');
      opt.value = option.id;
      opt.textContent = option.label;
      centerDropdown.appendChild(opt.cloneNode(true)); // Clone for reuse
      blacklistDropdown.appendChild(opt);
    });
  } catch (error) {
    console.error('Error loading dropdown options:', error);
  }
});
