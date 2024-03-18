import { Given, When, Then } from '@cucumber/cucumber';
import { test, expect } from '@playwright/test';
import { ICustomWorld } from '../support/custom-world';

Given('Eu estou na página de busca', async function (this: ICustomWorld) {
  await this.page!.goto('http://localhost:4200/search-page');
});

When('Eu preencho o formulário de busca', {timeout: 60 * 1000}, async function (this: ICustomWorld) {
  await this.page!.fill('#location', 'Recife');
  await this.page!.fill('#checkin', '2024-03-12');
  await this.page!.fill('#checkout', '2024-03-15');
  await this.page!.fill('#guests', '2');
});

When('Eu clico no botão de busca', async function (this: ICustomWorld) {
  await this.page!.click('button[type="submit"]');
});

Then('Eu vejo os resultados da busca', async function (this: ICustomWorld) {
  await this.page!.waitForSelector('.search-results');
  expect(await this.page!.isVisible('.search-results')).toBeTruthy();
});