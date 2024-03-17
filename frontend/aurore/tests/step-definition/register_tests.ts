import { Given, When, Then } from '@cucumber/cucumber';
import { expect } from '@playwright/test';
import { ICustomWorld } from '../support/custom-world';

Given('Estou na tela de "Cadastro de usuário"', async function (this: ICustomWorld) {
    await this.page!.goto('http://localhost:4200/users/create');
});
  
When('Eu tento cadastrar um usuário com Nome {string}, Username {string}, Email {string} , CPF {string} e senha {string}', async function (this: ICustomWorld, name, username, email, cpf, password) {
    await this.page!.fill('.form-control-name' , name);
    await this.page!.fill('.form-control-username' , username);
    await this.page!.fill('.form-control-email' , email);
    await this.page!.fill('.form-control-cpf' , cpf);
    await this.page!.fill('.form-control-password' , password);
    await this.page!.click('.btn-register')
});

Then('Continuo na tela de "Cadastro de usuário"', async function (this: ICustomWorld) {
    await expect(this.page!).toHaveURL('http://localhost:4200/users/create');
});  
Then('Vejo uma mensagem de erro: {string}', async function (this: ICustomWorld, message) {
    const text = await this.page!.innerText('.text-danger');
    expect(text).toBe(message);
});

