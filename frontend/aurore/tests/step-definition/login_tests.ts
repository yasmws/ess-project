import { Given, When, Then } from '@cucumber/cucumber';
import { expect } from '@playwright/test';
import { ICustomWorld } from '../support/custom-world';

Given('O banco de dados do sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "12345678912" e senha "12345678"', async function (this: ICustomWorld) {});
Given('Estou na tela "Login de usuário"', async function (this: ICustomWorld) {
    await this.page!.goto('http://localhost:4200/users/login');
});
  
When('Tento fazer login com Username {string} e senha {string}', async function (this: ICustomWorld, username, password) {
    await this.page!.fill('.form-control-username' , username);
    await this.page!.fill('.form-control-password' , password);
    await this.page!.click('.btn-login')
});

Then('Continuo na tela de "Login de usuário"', async function (this: ICustomWorld) {
    await expect(this.page!).toHaveURL('http://localhost:4200/users/login');
});  
Then('Vejo uma mensagem de {string}', async function (this: ICustomWorld, message) {
    const locator = this.page!.locator('.success-text');
    await expect(locator).toBeVisible();
    
    const text = await this.page!.innerText('.success-text');
    expect(text).toBe(message);
});

