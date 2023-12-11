## Projeto de ESS

### Backend:

#### Instalação:
- Vá até a pasta **backend** e execute o comando `pip install -r requirements.txt` para instalar as dependências do projeto.

#### Execução:
- `uvicorn main:app --reload` para executar o servidor.

#### Documentação:
- Para entender mais sobre fastAPI, veja a documentação oficial: https://fastapi.tiangolo.com/
- Para acessar a documentação da API, acesse: http://127.0.0.1:8000/docs#/
- Outra opção é acessar: http://127.0.0.1:8000/redoc

### FrontEnd:

#### Instalação:

- Para a configuração do ambiente local, faz-se necessário a instalação da versão do Node js mais atualizado na sua máquina

[Site para instalaão (RECOMENDADO A VERSÃO LTS)](https://nodejs.org/en)

- Em seu prompt de preferencia digite `ng install -g @angular/cli@16.2.10` ou em caso de sistema operacional tipo linux faça em modo `sudo` para dar permissão como administrador

``` javascript

    ng version // conferir se foi corretamente instalado
```


- Em seu prompt de preferencia digite `nps start` ou `ng serve` para que o projeto seja compilado e esteja disponível para visualização

``` javascript
// npm start
```

- Em seu browser pesquise por `localhost:4200`, essa é a porta padrão para projetos em

