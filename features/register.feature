Feature: Register

#Cenários de GUI

Scenario: Cadastro de usuário
Given O sistema não tem cadastrado um usuário com Nome "Pedro",  Email "phagp@cin.ufpe.br" e CPF "123456789-12"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "123456789-12" e senha "1234"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de "Cadastro realizado com sucesso"
And O usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "123456789-12" e senha "1234" é cadastrado no sistema

Scenario: Cadastro de usuário com username e senha já cadastrado
Given O sistema não tem cadastrado um usuário com Nome "Pedro", Email "phagp@cin.ufpe.br" e CPF "123456789-12"
And O sistema tem cadastrado um usuário com Nome "Paulo", Username "phagp", Email "phagp2@cin.ufpe.br" , CPF "124476799-12" e senha "1234"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "123456789-12" e senha "1234"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de "Cadastro realizado com sucesso"
And O usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "123456789-12" e senha "1234" é cadastrado no sistema

Scenario: Usuário tentou cadastrar um email já cadastrado 
Given O sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "123456789-12" e senha "1234"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Paulo", Username "phagp2", Email "phagp@cin.ufpe.br" , CPF "124476799-12" e senha "12345"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "Email já cadastrado"
And O usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "123456789-12" e senha "1234" continua cadastrado no sistema
And O usuário com Nome "Paulo", Username "phagp2", Email "phagp@cin.ufpe.br" , CPF "124476799-12" e senha "12345" não é cadastrado no sistema

Scenario: Usuário tentou cadastrar um CPF já cadastrado 
Given O sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "123456789-12" e senha "1234"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Paulo", Username "phagp2", Email "phagp2@cin.ufpe.br" , CPF "123456789-12" e senha "12345"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "CPF já cadastrado"
And O usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "123456789-12" e senha "1234" continua cadastrado no sistema
And O usuário com Nome "Paulo", Username "phagp2", Email "phagp2@cin.ufpe.br" , CPF "123456789-12" e senha "12345" não é cadastrado no sistema

Scenario: Usuário tentou cadastrar um nome já cadastrado 
Given O sistema tem cadastrado um usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "123456789-12" e senha "1234"
And Estou na tela de "Cadastro de usuário"
When Eu tento cadastrar um usuário com Nome "Pedro", Username "phagp2", Email "phagp2@cin.ufpe.br" , CPF "124476799-12" e senha "12345"
Then Continuo na tela de "Cadastro de usuário"
And Vejo uma mensagem de erro: "Nome já cadastrado"
And O usuário com Nome "Pedro", Username "phagp", Email "phagp@cin.ufpe.br" , CPF "123456789-12" e senha "1234" continua cadastrado no sistema
And O usuário com Nome "Pedro", Username "phagp2", Email "phagp2@cin.ufpe.br" , CPF "124476799-12" e senha "12345" não é cadastrado no sistema

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
