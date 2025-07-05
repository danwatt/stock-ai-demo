// Test for the S&P 500 Presidential Term Comparison page
describe('S&P 500 Presidential Term Comparison Page', () => {
  beforeEach(() => {
    // Visit the presidential comparison page before each test
    cy.visit('/presidential_comparison.html');
    // Wait for charts to load
    cy.wait(1000);
  });

  it('should load the page successfully', () => {
    // Check if the page has loaded
    cy.get('body').should('be.visible');
    cy.get('.chart-container').should('be.visible');
  });

  it('should display the correct page title', () => {
    // Check the page title in the browser
    cy.title().should('eq', 'S&P 500 Presidential Term Comparison');
  });

  it('should display the main heading', () => {
    // Check the main heading on the page
    cy.get('h1').should('contain', 'S&P 500 Presidential Term Comparison');
  });

  it('should have a chart container with chart', () => {
    // Check if the chart container exists and has a canvas
    cy.get('.chart-container canvas').should('be.visible');
  });

  it('should have navigation options', () => {
    // Check if the navigation links exist
    cy.get('.nav-link').should('have.length.at.least', 2);
    cy.get('.nav-link').should('contain', 'Indices Chart');
    cy.get('.nav-link').should('contain', 'Presidential Comparison');
  });

  it('should display the chart description', () => {
    // Check if the chart description exists
    cy.get('.description').should('be.visible');
    cy.get('.description').should('contain', 'This chart shows S&P 500 performance');
  });

  it('should have a legend for presidents', () => {
    // Check if the legend exists
    cy.get('.legend-container').should('be.visible');
    cy.get('.legend-item').should('have.length.at.least', 4); // At least 4 presidents
  });

  it('should show percentage labels on the y-axis', () => {
    // Check if the chart has percentage labels
    cy.get('.chart-container').should('contain', '%');
  });
});
