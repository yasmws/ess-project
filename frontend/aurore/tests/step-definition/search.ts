import { Given, When, Then } from '@cucumber/cucumber';
import { test, expect } from '@playwright/test';
import { ICustomWorld } from '../support/custom-world';

Given('Estou na tela "Busca de acomodações"', async function (this: ICustomWorld) {
  await this.page!.goto('http://localhost:4200/search');
});

When('Clico no botão de busca', async function (this: ICustomWorld) {
  await this.page!.click('.search-button');
});

Then('Vejo os resultados da busca com acomodações disponíveis', {timeout: 60 * 1000}, async function (this: ICustomWorld) {
    // Espera até que a URL contenha "/home"
    await this.page!.waitForURL(/\/home/);
    await this.page!.waitForLoadState('networkidle');

    const accommodationContainer = await this.page!.$('.accommodations-container');
    expect(accommodationContainer).not.toBeNull();
});

When('Preencho o formulário de busca com Localização {string}', async function (this: ICustomWorld, location: string) {
  await this.page!.fill('#location', location);
});

When('Preencho o formulário de busca com Localização {string}, Check-in {string}, Check-out {string} e Número de Hóspedes {string}', {timeout: 60 * 1000}, async function (this: ICustomWorld, location: string, checkin: string, checkout: string, guests: string) {
  await this.page!.fill('#location', location);
  await this.page!.fill('#checkin', checkin);
  await this.page!.fill('#checkout', checkout);
  await this.page!.fill('#guests', guests);
});

Then('Vejo uma mensagem de erro indicando que a data de check-in é maior que a data de check-out', {timeout: 60 * 1000}, async function (this: ICustomWorld) {
  expect(await this.page!.isVisible('.error-message')).toBeTruthy();
});
