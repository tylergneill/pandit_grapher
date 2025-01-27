export async function refreshDropdowns(authorsDropdown, worksDropdown) {
    try {
        const [authorsRes, worksRes] = await Promise.all([
            fetch('/api/entities/authors'),
            fetch('/api/entities/works')
        ]);

        const [optionsAuthors, optionsWorks] = await Promise.all([
            authorsRes.json(),
            worksRes.json()
        ]);

        authorsDropdown.empty();
        worksDropdown.empty();

        optionsAuthors.forEach(({ id, label }) => {
            authorsDropdown.append(new Option(label, id));
        });

        optionsWorks.forEach(({ id, label }) => {
            worksDropdown.append(new Option(label, id));
        });

        authorsDropdown.trigger('change');
        worksDropdown.trigger('change');
    } catch (error) {
        console.error('Error refreshing dropdowns:', error);
    }
}

document.addEventListener('DOMContentLoaded', async () => {
  try {
    // Fetch data for dropdowns
    const [authorsRes, worksRes] = await Promise.all([
      fetch('/api/entities/authors'),
      fetch('/api/entities/works')
    ]);

    const [optionsAuthors, optionsWorks] = await Promise.all([
      authorsRes.json(),
      worksRes.json()
    ]);

    // Get elements
    const authorsDropdown = document.getElementById('authors-dropdown');
    const worksDropdown = document.getElementById('works-dropdown');
    const excludeDropdown = document.getElementById('exclude-list-dropdown');
    const hopsInput = document.getElementById('hops');

    // Populate dropdowns
    populateDropdown(authorsDropdown, optionsAuthors);
    populateDropdown(worksDropdown, optionsWorks);
    populateDropdown(excludeDropdown, [...optionsAuthors, ...optionsWorks]);

    // Initialize Select2
    initializeSelect2('#authors-dropdown', 'Authors to include');
    initializeSelect2('#works-dropdown', 'Works to include');
    initializeSelect2('#exclude-list-dropdown', 'Entities to not expand');

    // Remove pre-initialization class
    document.querySelectorAll('.select2-initial').forEach(el => el.classList.remove('select2-initial'));

    // Initial width adjustment
    adjustWidths();

    // Handle window resizing
    window.addEventListener('resize', adjustWidths);

  } catch (error) {
    console.error('Error during initialization:', error);
  }
});

// Populate dropdown options
function populateDropdown(dropdown, options) {
  options.forEach(({ id, label }) => {
    const option = new Option(label, id);
    dropdown.add(option);
  });
}

// Initialize Select2 with placeholder
function initializeSelect2(selector, placeholder) {
  $(selector).select2({
    placeholder: placeholder,
    allowClear: true,
    tags: false,
    width: 'resolve' // Ensure the dropdown width is dynamic
  });
}

// Adjust both Select2 and Hops widths
function adjustWidths() {
  try {
    // Update Select2 widths
    $('#authors-dropdown').select2('destroy').select2({ placeholder: 'Authors to include', allowClear: true, width: 'resolve' });
    $('#works-dropdown').select2('destroy').select2({ placeholder: 'Works to include', allowClear: true, width: 'resolve' });
    $('#exclude-list-dropdown').select2('destroy').select2({ placeholder: 'Entities to not expand', allowClear: true, width: 'resolve' });

    // Match Hops width to Works dropdown
    const worksContainer = document.querySelector('#works-dropdown + .select2-container');
    const hopsInput = document.getElementById('hops');

    if (worksContainer) {
      const worksWidth = worksContainer.offsetWidth;
      hopsInput.style.width = `${worksWidth}px`;
    } else {
      console.warn('Works container not found.');
    }
  } catch (error) {
    console.error('Error adjusting widths:', error);
  }
}
