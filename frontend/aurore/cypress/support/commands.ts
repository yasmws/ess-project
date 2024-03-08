declare global {
    // eslint-disable-next-line @typescript-eslint/no-namespace
    namespace Cypress {
        interface Chainable {
            getDataCy(dataCySelector: string): Chainable<JQuery<HTMLElement>>;
        }
    }
}

Cypress.Commands.add('getDataCy', dataCySelector => {
    return cy.get(`[dataCy="${dataCySelector}"]`);
});

export {};