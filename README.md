## Aurore

### Backend:
O backend deste projeto foi desenvolvido com [FastAPI](https://fastapi.tiangolo.com/), um framework web para construção de APIs com Python.
O banco de dados utilizado foi o [Google Firebase](https://firebase.google.com/).

#### Instalação:
- Vá até a pasta **backend** e execute o comando `pip install -r requirements.txt` para instalar as dependências do projeto.

#### Execução:
- Dentro de /backend, utilize o comando `uvicorn main:app --reload` para executar o servidor.

#### Documentação:
- Para entender mais sobre fastAPI, veja a documentação oficial: https://fastapi.tiangolo.com/
- Para acessar a documentação da API, acesse: http://127.0.0.1:8000/docs#/
- Outra opção é acessar: http://127.0.0.1:8000/redoc

### Frontend:

Este projeto foi gerado com [Angular CLI](https://github.com/angular/angular-cli) versão 16.2.10.

#### Instalação:

- Para a configuração do ambiente local, faz-se necessário a instalação da versão do Node js mais atualizado na sua máquina

[Site para instalação (RECOMENDADO A VERSÃO LTS)](https://nodejs.org/en)

- Em seu prompt de preferência digite `ng install -g @angular/cli@16.2.10` ou em caso de sistema operacional tipo linux faça em modo `sudo` para dar permissão como administrador

``` javascript
    ng version // conferir se foi corretamente instalado
```

- Para rodar, antes, é preciso ir até o **aurore** para funcionar. Ou seja,

``` javascript
    cd frontend/aurore
```

- Em seu prompt de preferencia digite `npm start` ou `ng serve` para que o projeto seja compilado e esteja disponível para visualização

``` javascript
    npm start
```

``` javascript
    ng serve
```

- Em seu browser acesse `http://localhost:4200/`, para ver a aplicação rodando. A aplicação irá recarregar automaticamente caso haja alguma alteração no código fonte.

- Você pode testar rodando 
 
``` javascript
    npx cypress open
```
- Caso tenha problemas com o cypress, rode a aplicação e, com ela ainda em execução, em um outro terminal, rode o cypress. Isso deve resolver.

No meu caso, tive problemas com o comando de npm install também e, para tanto, passei a utilizar o yarn. O comando é similar:

``` javascript
    yarn install
```

