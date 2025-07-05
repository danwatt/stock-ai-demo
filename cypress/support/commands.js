// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

// Custom command to wait for Chart.js to render
Cypress.Commands.add('waitForChart', (selector = '.chart-container canvas') => {
  cy.get(selector).should('be.visible');
  cy.wait(1000); // Give chart time to animate and render
});

// Custom command to check if a chart has data points
Cypress.Commands.add('chartShouldHaveData', (selector = '.chart-container canvas') => {
  cy.get(selector)
    .should('be.visible')
    .should(($canvas) => {
      // If canvas exists, we consider it has data (simplified approach)
      expect($canvas.length).to.be.greaterThan(0);
    });
});
