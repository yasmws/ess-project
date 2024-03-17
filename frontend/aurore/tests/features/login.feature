Feature: Login

#Cenários de GUI

Scenario: Login do usuário usando username
Given O banco de dados do sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "12345678912" e senha "12345678"
And Estou na tela "Login de usuário"
When Tento fazer login com Username "phagp" e senha "12345678"
Then Continuo na tela de "Login de usuário"
And Vejo uma mensagem de "Usuário logado com sucesso!"