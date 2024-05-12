// Get the search section and the featured products and promotions sections
const searchSection = document.querySelector(".search");
const featuredProductsSection = document.querySelector(".featured-products");
const promotionsSection = document.querySelector(".promotions");

// Calculate the height of the search results table and adjust the position of the other sections
function adjustSectionPositions() {
  const searchResultsTable = document.querySelector(".search table");
  if (searchResultsTable) {
    const searchResultsTableHeight = searchResultsTable.offsetHeight;
    featuredProductsSection.style.marginTop = `calc(2rem + ${searchResultsTableHeight}px)`;
    promotionsSection.style.marginTop = `calc(2rem + ${searchResultsTableHeight}px)`;
  } else {
    featuredProductsSection.style.marginTop = "2rem";
    promotionsSection.style.marginTop = "2rem";
  }
}

// Call the adjustSectionPositions function on page load and on window resize
window.addEventListener("load", adjustSectionPositions);
window.addEventListener("resize", adjustSectionPositions);
