// Test for the Market Indices Historical Data Chart page
describe("Market Indices Historical Data Chart Page", () => {
  beforeEach(() => {
    // Visit the index page before each test
    cy.visit("/index.html");
    // Wait for charts to load - charts usually take a bit longer
    cy.wait(1000);
  });

  it("should load the page successfully", () => {
    // Check if the page has loaded
    cy.get("body").should("be.visible");
    cy.get(".chart-container").should("be.visible");
  });

  it("should display the correct page title", () => {
    // Check the page title in the browser
    cy.title().should("eq", "Market Indices Historical Data Chart");
  });

  it("should display the main heading", () => {
    // Check the main heading on the page
    cy.get("h1").should(
      "contain",
      "Market Indices - Historical Closing Prices",
    );
  });

  it("should have date range sliders", () => {
    // Check if the date range sliders exist
    cy.get("#startDateSlider").should("exist");
    cy.get("#endDateSlider").should("exist");
  });

  it("should display the date range", () => {
    // Check if the date range display exists
    cy.get(".date-display").should("be.visible");
  });

  it("should have a chart container with chart", () => {
    // Check if the chart container exists and has a canvas
    cy.get(".chart-container canvas").should("be.visible");
  });

  it("should have navigation options", () => {
    // Check if the navigation links exist
    cy.get(".btn-group a").should("have.length.at.least", 2);
    cy.get(".btn-group a").should("contain", "View Market Indices");
    cy.get(".btn-group a").should("contain", "View Presidential Comparison");
  });

  it("should have president legend", () => {
    // Check if the president legend exists
    cy.get("#presidents-legend").should("be.visible");
    cy.get(".president-item").should("have.length.at.least", 4); // At least 4 presidents
  });

  it("should have preset range buttons", () => {
    // Check if the preset range buttons exist
    cy.get("#preset-ranges button").should("have.length.at.least", 4);
  });
});
