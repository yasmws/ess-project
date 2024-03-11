Feature: Register

#Cenários de GUI

Scenario: Cadastro de usuário
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Paulo", Username "plop", Email "plop@cin.ufpe.br" , CPF "12345678905" e senha "12345678"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de "Usuário criado!"

Scenario: Usuário tentou cadastrar um nome com números
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Paulo12", Username "plop", Email "plop@cin.ufpe.br" , CPF "12345678905" e senha "12345678"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "Nome só deve conter letras."

Scenario: Usuário tentou cadastrar um username com dígitos especiais
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Paulo", Username "plop@", Email "plop@cin.ufpe.br" , CPF "12345678905" e senha "12345678"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "Username só deve conter caracteres alfanuméricos."

Scenario: Usuário tentou cadastrar um email em formato inválido
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Paulo", Username "plop", Email "plopcin.ufpe.br" , CPF "12345678905" e senha "12345678"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "Esse email é inválido."

Scenario: Usuário tentou cadastrar um CPF em formato inválido
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Paulo", Username "plop", Email "plop@cin.ufpe.br" , CPF "012345678905" e senha "12345678"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "CPF está no formato inválido."

Scenario: Usuário tentou cadastrar uma senha com menos de 8 caracteres
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Paulo", Username "plop", Email "plop@cin.ufpe.br" , CPF "12345678905" e senha "1234567"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "Senha deve conter pelo menos 8 caracteres."

Scenario: Usuário tentou cadastrar um username já cadastrado 
Given O banco de dados do sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "12345678912" e senha "12345678"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Pedro", Username "phagp", Email "phagp2@cin.ufpe.br" , CPF "12447678912" e senha "12345678"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "Username já existe."

Scenario: Usuário tentou cadastrar um email já cadastrado 
Given O banco de dados do sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "12345678912" e senha "12345678"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Pedro", Username "phagp2", Email "phagp@cin.ufpe.br" , CPF "12447678912" e senha "12345678"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "Email já existe."

Scenario: Usuário tentou cadastrar um CPF já cadastrado 
Given O banco de dados do sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "12345678912" e senha "12345678"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Pedro", Username "phagp2", Email "phagp2@cin.ufpe.br" , CPF "12345678912" e senha "12345678"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "CPF já existe."

#Cenários de serviço

Scenario: Cadastro de usuário
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
When Uma requisição POST é enviada para "/users/create" com Nome "Paulo", Username "plop", Email "plop@cin.ufpe.br" , CPF "12345678905" e senha "12345678"
Then O status da resposta deve ser "201"
And A resposta deve conter "Usuário criado!"

Scenario: Usuário tentou cadastrar um nome com números
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
When Uma requisição POST é enviada para "/users/create" com Nome "Paulo12", Username "plop", Email "plop@cin.ufpe.br" , CPF "12345678905" e senha "12345678"
Then O status da resposta deve ser "400"
And A resposta deve conter "Nome só deve conter letras."

Scenario: Usuário tentou cadastrar um username com dígitos especiais
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
When Uma requisição POST é enviada para "/users/create" com Nome "Paulo", Username "plop@", Email "plop@cin.ufpe.br" , CPF "12345678905" e senha "12345678"
Then O status da resposta deve ser "400"
And A resposta deve conter "Username só deve conter caracteres alfanuméricos."

Scenario: Usuário tentou cadastrar um email em formato inválido
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
When Uma requisição POST é enviada para "/users/create" com Nome "Paulo", Username "plop", Email "plopcin.ufpe.br" , CPF "12345678905" e senha "12345678"
Then O status da resposta deve ser "400"
And A resposta deve conter "Esse email é inválido."

Scenario: Usuário tentou cadastrar um CPF em formato inválido
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
When Uma requisição POST é enviada para "/users/create" com Nome "Paulo", Username "plop", Email "plop@cin.ufpe.br" , CPF "012345678905" e senha "12345678"
Then O status da resposta deve ser "400"
And A resposta deve conter "CPF está no formato inválido."

Scenario: Usuário tentou cadastrar uma senha com menos de 8 caracteres
Given O banco de dados do sistema não tem cadastrado um usuário com Username "plop", Email "plop@cin.ufpe.br" e CPF "12345678905"
When Uma requisição POST é enviada para "/users/create" com Nome "Paulo", Username "plop", Email "plop@cin.ufpe.br" , CPF "12345678905" e senha "1234567"
Then O status da resposta deve ser "400"
And A resposta deve conter "Senha deve conter pelo menos 8 caracteres."

Scenario: Usuário tentou cadastrar um username já cadastrado 
Given O banco de dados do sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "12345678912" e senha "12345678"
When Uma requisição POST é enviada para "/users/create" com Nome "Pedro", Username "phagp", Email "phagp2@cin.ufpe.br" , CPF "12447678912" e senha "12345678"
Then O status da resposta deve ser "400"
And A resposta deve conter "Username já existe."

Scenario: Usuário tentou cadastrar um email já cadastrado 
Given O banco de dados do sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "12345678912" e senha "12345678"
When Uma requisição POST é enviada para "/users/create" com Nome "Pedro", Username "phagp2", Email "phagp@cin.ufpe.br" , CPF "12447678912" e senha "12345678"
Then O status da resposta deve ser "400"
And A resposta deve conter "Email já existe."

Scenario: Usuário tentou cadastrar um CPF já cadastrado 
Given O banco de dados do sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "12345678912" e senha "12345678"
When Uma requisição POST é enviada para "/users/create" com Nome "Pedro", Username "phagp2", Email "phagp2@cin.ufpe.br" , CPF "12345678912" e senha "12345678"
Then O status da resposta deve ser "400"
And A resposta deve conter "CPF já existe."
