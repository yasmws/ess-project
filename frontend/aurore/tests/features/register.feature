Feature: Register

#Cenários de GUI

Scenario: Usuário tentou cadastrar um username com dígitos especiais
Given Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Paulo", Username "plop@", Email "plop@cin.ufpe.br" , CPF "12345678905" e senha "12345678"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "Username só deve conter caracteres alfanuméricos."