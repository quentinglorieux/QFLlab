document.addEventListener('DOMContentLoaded', function () {
    const publicationItems = document.querySelectorAll('.publi_div');
    const yearButtonsContainer = document.getElementById('yearButtonsContainer');
    
    const uniqueYears = ['all', ...new Set(Array.from(publicationItems).map(item => item.getAttribute('data-year')))];
    // Create buttons for each unique year
    uniqueYears.forEach(function (year) {
      const button = document.createElement('button');
      button.classList.add('btn');
      button.classList.add('year-button');
      button.setAttribute('data-year', year);

            // Count the number of publications for the current year
      const publicationCount = Array.from(publicationItems).filter(item => {
      const publicationYear = item.getAttribute('data-year');
       return year === 'all' || year === publicationYear;
      }).length;

      button.textContent = year === 'all' ? `All (${publicationCount})` : `${year} (${publicationCount})`;


      button.addEventListener('click', function () {
        const selectedYear = this.getAttribute('data-year');

        // Toggle the 'active' class for styling purposes
        document.querySelectorAll('.year-button').forEach(function (btn) {
          btn.classList.remove('active');
        });
        this.classList.add('active');

        publicationItems.forEach(function (publicationItem) {
          const publicationYear = publicationItem.getAttribute('data-year');
          // If the selected year is 'all' or matches the publication year, show the item; otherwise, hide it
          if (selectedYear === 'all' || selectedYear === publicationYear) {
            publicationItem.style.display = 'block';
            publicationItem.classList.remove('hide');
          } else {
            publicationItem.style.display = 'none';
            publicationItem.classList.add('hide');
          }
        });
      });
      yearButtonsContainer.appendChild(button);
    });
  });

