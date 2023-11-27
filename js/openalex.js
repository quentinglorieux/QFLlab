async function fetchDataAndDisplay() {
  try {
    let allResults = [];
    let currentPage = 1;

    let apiURL = 'https://api.openalex.org/works?'
    let OAID = 'A5024990264'
    let filters = 'has_doi:true,primary_location.source.has_issn:true'
    let sort = 'publication_date:desc'

    const apiContent = document.getElementById("api-content");

    while (true) {
      // Fetch data from the API for the current page
      const response = await fetch(
        `${apiURL}filter=authorships.author.id:${OAID},${filters}&sort=${sort}&page=${currentPage}`
      );
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      const results = data.results;

      if (currentPage == 1) {
        apiContent.innerHTML = ""
        const ul = document.createElement("ul");
        results.forEach((item) => {
          const li = document.createElement("li");
          li.textContent = item.title;
          ul.appendChild(li);
        });
        apiContent.appendChild(ul);
      }

      if (results.length === 0) {
        break;
      }

      allResults = allResults.concat(results);
      currentPage++;
    }

    apiContent.innerHTML = "";

    const ul = document.createElement("ul");
    allResults.forEach((item) => {
      const li = document.createElement("li");

      li.textContent = ` ${item.title} - ${ item.primary_location.source.display_name } (${item.publication_year}) `;
      ul.appendChild(li);
        
    });
    apiContent.appendChild(ul);

  } catch (error) {
    console.error("Error fetching or processing data:", error);
  }
}
