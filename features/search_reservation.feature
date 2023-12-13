Feature: Busca de reservas
    As um usuário   
    I want buscar reservas disponíveis
    So that eu possa encontrar o hotel ideal para a minha estadia

Scenario: Busca de reserva pela localização
Given que o usuário "Bruno" está logado
And "Bruno" está na tela de busca
When "Bruno" escreve a cidade "Recife" no campo de busca
And realiza a busca
Then Bruno é redirecionado para a tela de resultados

Scenario: Busca de reserva pelo nome do hotel
Given que o usuário "Bruno" está logado
And "Bruno" está na tela de busca
When "Bruno" escreve o nome do hotel "Hotel Boa viagem" no campo de busca
And realiza a busca
Then "Bruno" é redirecionado para a tela de resultados

Scenario: Busca de reserva pela localização com filtro de data
Given que o usuário "Bruno" está logado
And "Bruno" está na tela de busca
When "Bruno" escreve a cidade "Recife" no campo de busca
And realiza a busca
And seleciona a data de check-in "10/10/2024"
And seleciona a data de check-out "15/10/2024"
Then "Bruno" é redirecionado para a tela de resultados

Scenario: Busca de reserva sem disponibilidade
Given que o usuário "Bruno" está logado
And "Bruno" está na tela de busca
When "Bruno" escreve a cidade "Recife" no campo de busca
And realiza a busca
And seleciona a data de check-in "10/10/2024"
And seleciona a data de check-out "15/10/2024"
Then "Bruno" é redirecionado para a tela de resultados
And é exibida a mensagem "Sem disponibilidade de reservas para as datas selecionadas!", com status code "204"
