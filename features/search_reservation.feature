Feature: Busca de reservas
    As um usuário   
    I want buscar reservas disponíveis
    So that eu possa encontrar o hotel ideal para a minha estadia

Scenario: Busca de reserva pela localização
Given que o Usuário "Bruno" está logado com o Username "bruno12", Email "bruno@gmail.com" e Senha "123456"
And "Bruno" está na tela de busca
When "Bruno" escreve a cidade "Recife" no campo de busca
And seleciona a opção "Buscar"
Then Bruno é redirecionado para a tela de resultados

Scenario: Busca de reserva pelo nome do hotel
Given que o Usuário "Bruno" está logado com o Username "bruno12", Email "bruno@gmail.com" e Senha "123456"
And "Bruno" está na tela de busca
When "Bruno" escreve o nome do hotel "Hotel Boa viagem" no campo de busca
And seleciona a opção "Buscar"
Then "Bruno" é redirecionado para a tela de resultados

Scenario: Busca de reserva pela localização com filtro de data
Given que o Usuário "Bruno" está logado com o Username "bruno12", Email "bruno@gmail.com" e Senha "123456"
And "Bruno" está na tela de busca
When "Bruno" escreve a cidade "Recife" no campo de busca
And seleciona a opção "Buscar"
And seleciona a data de check-in "10/10/2024"
And seleciona a data de check-out "15/10/2024"
Then "Bruno" é redirecionado para a tela de resultados

Scenario: Busca de reserva sem disponibilidade
Given que o Usuário "Bruno" está logado com o Username "bruno12", Email "bruno@gmail.com" e Senha "123456"
And "Bruno" está na tela de busca
When "Bruno" escreve a cidade "Recife" no campo de busca
And seleciona a opção "Buscar"
And seleciona a data de check-in "10/10/2024"
And seleciona a data de check-out "15/10/2024"
Then "Bruno" é redirecionado para a tela de resultados
And é exibida a mensagem "Sem disponibilidade de reservas para as datas selecionadas!", com status code "204"
