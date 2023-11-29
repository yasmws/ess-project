Feature: Login

Scenario: Login do usuário
Given O sistema tem cadastrado um usuário com Nome “Pedro”, Username “phagp”, Email “phagp@cin.ufpe.br” , CPF “123456789-12” e senha “1234”
And Estou na tela “Login de usuário”
When Tento fazer login com Username “phagp”, Email “phagp@cin.ufpe.br” e senha “1234”
Then Continuo na tela de “Login de usuário”
And Vejo uma mensagem de ”Login realizado com sucesso”
And Eu estou logado no sistema

Scenario: Usuário informou senha incorretamente durante o login 
Given O sistema tem cadastrado um usuário com Nome “Pedro”, Username “phagp”, Email “phagp@cin.ufpe.br” , CPF “123456789-12” e senha “1234”
And Estou na tela “Login de usuário”
When Tento fazer login com Username “phagp”, Email “phagp@cin.ufpe.br” e senha “12345”
Then Continuo na tela de “Login de usuário”
And Vejo uma mensagem de erro sobre senha incorreta
And Eu continuo não estando logado ao sistema