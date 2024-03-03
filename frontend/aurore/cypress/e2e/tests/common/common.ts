import { Given } from '@badeball/cypress-cucumber-preprocessor';

const HOME = 'home';

Given('o usuário está na página {string}', (page: string) => {
    if (page === HOME) page = '/';

    cy.visit(page);
});