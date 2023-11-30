Feature: Register

Scenario: Cadastro de usuário
Given O sistema não tem cadastrado um usuário com Nome “Pedro”,  Email “phagp@cin.ufpe.br” e CPF “123456789-12”
And Estou na tela de “Cadastro de usuário”
When Eu tento cadastrar um usuário com Nome “Pedro”, Username “phagp”, Email “phagp@cin.ufpe.br” , CPF “123456789-12” e senha “1234”
Then Continuo na tela de “Cadastro de usuário”
And Vejo uma mensagem de “Cadastro realizado com sucesso”
And O usuário com Nome “Pedro”, Username “phagp”, Email “phagp@cin.ufpe.br” , CPF “123456789-12” e senha “1234” é cadastrado no sistema

Scenario: Usuário tentou cadastrar um email já cadastrado 
Given O sistema tem cadastrado um usuário com Nome “Pedro”, Username “phagp”, Email “phagp@cin.ufpe.br” , CPF “123456789-12” e senha “1234”
And Estou na tela de “Cadastro de usuário”
When Eu tento cadastrar um usuário com Nome “Paulo”, Username “phagp2”, Email “phagp@cin.ufpe.br” , CPF “124476789-12” e senha “12345”
Then Continuo na tela de “Cadastro de usuário”
And Vejo uma mensagem de erro sobre email já cadastrado
And O usuário com Nome “Pedro”, Username “phagp”, Email “phagp@cin.ufpe.br” , CPF “123456789-12” e senha “1234” continua cadastrado no sistema
And O usuário com Nome “Paulo”, Username “phagp2”, Email “phagp@cin.ufpe.br” , CPF “124476789-12” e senha “12345” não é cadastrado no sistema

Scenario: Usuário tentou cadastrar um CPF já cadastrado 
Given O sistema tem cadastrado um usuário com Nome “Pedro”, Username “phagp”, Email “phagp@cin.ufpe.br” , CPF “123456789-12” e senha “1234”
And Estou na tela de “Cadastro de usuário”
When Eu tento cadastrar um usuário com Nome “Paulo”, Username “phagp2”, Email “phagp2@cin.ufpe.br” , CPF “123456789-12” e senha “12345”
Then Continuo na tela de “Cadastro de usuário”
And Vejo uma mensagem de erro sobre CPF já cadastrado
And O usuário com Nome “Pedro”, Username “phagp”, Email “phagp@cin.ufpe.br” , CPF “123456789-12” e senha “1234” continua cadastrado no sistema
And O usuário com Nome “Paulo”, Username “phagp2”, Email “phagp2@cin.ufpe.br” , CPF “123456789-12” e senha “12345” não é cadastrado no sistema

Scenario: Usuário tentou cadastrar um nome já cadastrado 
Given O sistema tem cadastrado um usuário com Nome “Pedro”, Username “phagp”, Email “phagp@cin.ufpe.br” , CPF “123456789-12” e senha “1234”
And Estou na tela de “Cadastro de usuário”
When Eu tento cadastrar um usuário com Nome “Pedro”, Username “phagp2”, Email “phagp2@cin.ufpe.br” , CPF “124476789-12” e senha “12345”
Then Continuo na tela de “Cadastro de usuário”
And Vejo uma mensagem de erro sobre nome já cadastrado
And O usuário com Nome “Pedro”, Username “phagp”, Email “phagp@cin.ufpe.br” , CPF “123456789-12” e senha “1234” continua cadastrado no sistema
And O usuário com Nome “Pedro”, Username “phagp2”, Email “phagp2@cin.ufpe.br” , CPF “124476789-12” e senha “12345” não é cadastrado no sistema