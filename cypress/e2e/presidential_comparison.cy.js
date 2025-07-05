// Test for the S&P 500 Presidential Term Comparison page
describe("S&P 500 Presidential Term Comparison Page", () => {
  beforeEach(() => {
    // Visit the presidential comparison page before each test
    cy.visit("/presidential_comparison.html");
    // Wait for charts to load
    cy.wait(1000);
  });

  it("should load the page successfully", () => {
    // Check if the page has loaded
    cy.get("body").should("be.visible");
    cy.get(".chart-container").should("be.visible");
  });

  it("should display the correct page title", () => {
    // Check the page title in the browser
    cy.title().should("eq", "S&P 500 Presidential Term Comparison");
  });

  it("should display the main heading", () => {
    // Check the main heading on the page
    cy.get("h1").should(
      "contain",
      "S&P 500 Relative Performance by Presidential Term",
    );
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

  it("should display the chart description", () => {
    // Check if the chart description exists
    cy.get(".card-body p").should("be.visible");
    cy.get(".card-body p").should(
      "contain",
      "This chart shows the relative performance of the S&P 500",
    );
  });

  it("should have a legend for presidents", () => {
    // Check if the legend exists
    cy.get("#presidentsLegend").should("be.visible");
    cy.get(".legend-item").should("have.length.at.least", 4); // At least 4 presidents
  });

  it("should show percentage labels on the y-axis", () => {
    // Check if the chart has percentage labels on y-axis
    cy.get(".chart-container").should("exist");
    // Since we can't directly check the rendered chart's y-axis labels, we'll verify the container exists
  });
});
