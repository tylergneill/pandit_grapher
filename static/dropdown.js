document.addEventListener('DOMContentLoaded', async () => {
  try {
    const [authorsRes, worksRes] = await Promise.all([
      fetch('/api/entities/authors'),
      fetch('/api/entities/works')
    ]);

    const [optionsAuthors, optionsWorks] = await Promise.all([
      authorsRes.json(),
      worksRes.json()
    ]);

    const authorsDropdown = document.getElementById('authors-dropdown');
    const worksDropdown = document.getElementById('works-dropdown');
    const excludeDropdown = document.getElementById('exclude-list-dropdown');

    populateDropdown(authorsDropdown, optionsAuthors);
    populateDropdown(worksDropdown, optionsWorks);
    populateDropdown(excludeDropdown, [...optionsAuthors, ...optionsWorks]);

    // Initialize Select2 after options are ready
    $('#authors-dropdown, #works-dropdown, #exclude-list-dropdown').select2({
      placeholder: 'Select an option',
      allowClear: true
    });

    // Clean up .select2-initial class
    document.querySelectorAll('.select2-initial').forEach(el => el.classList.remove('select2-initial'));
  } catch (error) {
    console.error('Error initializing dropdowns:', error);
  }
});

function populateDropdown(dropdown, options) {
  options.forEach(({ id, label }) => {
    const option = new Option(label, id);
    dropdown.add(option);
  });
}
