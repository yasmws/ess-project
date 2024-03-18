import { CustomWorld } from '../support/custom-world';
import { Given, When, Then, After, Before } from '@cucumber/cucumber';
import { chromium, Page, Browser} from '@playwright/test';
import { expect } from 'chai';
import { timeout } from 'rxjs';
import { ICustomWorld } from 'tests/support/custom-world';

let page: Page;
let browser: Browser;

Before(async () => {
    browser = await chromium.launch();
    page = await browser.newPage();
});

Given('O usuário {string} está logado e na página de pesquisa {string}', async function (this: ICustomWorld, usuario: string, pagina: string) {
    await this.page!.goto(`http://localhost:4200${pagina}`);
});

Given('O usuário é redirecionado para a página de {string}', async function (this: ICustomWorld, pagina: string) {
    const currentUrl = await this.page!.url();
    const Url = 'http://localhost:4200/book-acmdt'
    const firstCharacters = currentUrl.substring(0, Url.length);

    expect(firstCharacters).to.equal('http://localhost:4200/book-acmdt');
});

When('O usuário clica no botão de busca', async function (this: ICustomWorld) {
    // Aguarda até que o botão de busca esteja disponível na página
    await this.page!.waitForSelector('.search-container button');

    // Clica no botão de busca
    await this.page!.click('.search-container button');
});

When('O usuário é redirecionado para a página {string}', { timeout: 60000 }, async function (this: ICustomWorld, pagina: string) {
    const timeoutMilliseconds = 60000;
    const startTime = new Date().getTime();

    // Loop de espera para verificar continuamente se o URL corresponde à página esperada
    while (new Date().getTime() - startTime < timeoutMilliseconds) {
        const currentUrl = await this.page!.url();
        if (currentUrl === `http://localhost:4200${pagina}?checkin=&checkout=`) {
            return;
        }
        await this.page!.waitForTimeout(1000);
    }
    throw new Error(`Redirecionamento para a página ${pagina} não ocorreu dentro do tempo limite de ${timeoutMilliseconds} ms`);
});

When('O usuário clica na primeira acomodação disponível', { timeout: 600000 }, async function (this: ICustomWorld) {
    try {
        // Aguarda até que a primeira acomodação esteja disponível na página
        await this.page!.waitForSelector('.accommodations-container .accommodation', { timeout: 600000 });
        const accommodations = await this.page!.$$('.accommodations-container .accommodation');

        // Verifica se há pelo menos uma acomodação disponível
        if (accommodations.length > 0) {
            // Obtém a primeira acomodação
            const firstAccommodation = accommodations[0];

            // Clica na primeira acomodação disponível
            await firstAccommodation.click();
        } else {
            throw new Error('Nenhuma acomodação disponível encontrada na página');
        }
    } catch (error) {
        throw new Error(`Erro ao clicar na primeira acomodação disponível: ${error}`);
    }
});


When('O usuário clica no botão {string}', async function (this: ICustomWorld, botao: string) {
    // Aguarda até que o botão de reserva esteja disponível na página
    await this.page!.waitForSelector('button[type="submit"]');

    // Clica no botão de reserva
    await this.page!.click('button[type="submit"]');
});




Then('O usuário deve ser redirecionado para a página de {string}', async function (this: ICustomWorld, pagina:string) {
    const currentUrl = await this.page!.url();
    expect(currentUrl).to.equal('http://localhost:4200/home');
});

Then('O formulário não é enviado', async function (this: ICustomWorld) {
    const currentUrl = await this.page!.url();
    expect(currentUrl).to.equal('http://localhost:4200/home')
})

After(async () => {
    await browser.close();
});
