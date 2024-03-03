import { When, Then } from '@badeball/cypress-cucumber-preprocessor';

When(
    'o usuário preenche o campo {string} com {string}',
    (field: string, value: string) => {
        cy.getDataCy(field).type(value);
    }
);

When('o usuário escolhe a opção {string}', (option: string) => {
    cy.getDataCy(option).click();
});

Then('o usuário vê a mensagem {string}', (text: string) => {
    cy.on('window:alert', str => {
        expect(str).to.equal(text);
    });
});

// Scenario: Visualizar itens
Then(
    'o usuário visualiza o item {string} de nome {string}',
    (id: string, name: string) => {
        cy.getDataCy(`item-${id}`).should('contain', name);
    }
);