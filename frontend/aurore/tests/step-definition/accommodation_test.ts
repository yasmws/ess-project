import { ToString } from './../../node_modules/type-fest/source/internal.d';
import { CustomWorld } from '../support/custom-world';
import { Given, When, Then, After, Before } from '@cucumber/cucumber';
import { chromium, Page, Browser} from '@playwright/test';
import { expect } from 'chai';
import { ICustomWorld } from 'tests/support/custom-world';

let page: Page;
let browser: Browser;

Before(async () => {
    browser = await chromium.launch();
    page = await browser.newPage();
});

Given('O usuário {string} está logado e na página de criar acomodação {string}', async function (this: ICustomWorld, usuario: string, pagina: string) {
    await this.page!.goto(`http://localhost:4200/${pagina}`); // Corrigido para usar a variável "pagina"
    // Implementar o login se necessário
});

When('Eu preencho os detalhes da acomodação com nome: {string}, localização: {string}, num de quartos: {string}, capacidade máxima: {string}, descrição: {string}, preco: {string}', async function (this: ICustomWorld, string, string2, string3, string4, string5, string6){
    await this.page!.fill('#nome', string);
    await this.page!.fill('#localizacao', string2);
    await this.page!.fill('#num_quartos', string3.toString());
    await this.page!.fill('#max_capacidade', string4.toString());
    await this.page!.fill('#descricao', string5);
    await this.page!.fill('#preco', string6.toString());
});

When('Eu clico no botão "Salvar"', async function (this: ICustomWorld) {
    await this.page!.click('button[type="submit"]');
});

When('Eu tento clicar no botão "Salvar"', async function (this: ICustomWorld) {
    const button = await this.page!.$('button[type="submit"]');
    const isDisabled = await button?.isEnabled();
    expect(isDisabled).to.be.false;
});

Then('Eu devo ser redirecionado para {string}', async function(this: ICustomWorld, url:string) {
    
    await this.page!.waitForURL(`http://localhost:4200${url}`);
});

Then('Eu devo não ser capaz de criar a acomodação', async function (this: ICustomWorld) {
    const currentUrl = await this.page!.url();
    expect(currentUrl).not.to.equal('http://localhost:4200/home');
});

After(async () => {
    await browser.close();
});
