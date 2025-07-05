// Test for the Vanguard Funds Historical Data Chart page
describe("Vanguard Funds Historical Data Chart Page", () => {
  beforeEach(() => {
    // Visit the funds page before each test
    cy.visit("/funds.html");
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
    cy.title().should("eq", "Vanguard Funds Historical Data Chart");
  });

  it("should display the main heading", () => {
    // Check the main heading on the page
    cy.get("h1").should(
      "contain",
      "Vanguard Funds - Historical Closing Prices",
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
    cy.get(".btn-group a").should("contain", "View Vanguard Funds");
  });

  it("should have fund selector", () => {
    // Check if the fund selector exists
    cy.get("#fundSelector").should("be.visible");
    cy.get('#fundSelector input[type="checkbox"]').should(
      "have.length.at.least",
      2,
    );
  });

  it("should have preset range buttons", () => {
    // Check if the preset range buttons exist
    cy.get('.btn-group[role="group"] button').should("have.length.at.least", 4);
  });
});
