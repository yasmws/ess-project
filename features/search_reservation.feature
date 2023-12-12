Feature: Busca de reservas
    As um usuário   
    I want buscar reservas disponíveis
    So that eu possa encontrar o hotel ideal para a minha estadia

Scenario: O usuário "Bruno" busca uma reserva pela localização
Given que Bruno está na tela de busca
When Bruno escreve a cidade "Recife" no campo de busca
And seleciona o botão de buscar
Then Bruno é redirecionado para a tela de resultados

Scenario: O usuário "Bruno" busca uma reserva pelo nome do hotel
Given que "Bruno" está na tela de busca
When "Bruno" escreve o nome do hotel "Hotel Boa viagem" no campo de busca
And seleciona o botão de buscar
Then "Bruno" é redirecionado para a tela de resultados

Scenario: O usuário "Ana" busca uma reserva pela localização com filtro de data
Given que "Ana" está na tela de busca
When "Ana" escreve a cidade "Recife" no campo de busca
And seleciona o botão de buscar
And seleciona a data de check-in "10/10/2024"
And seleciona a data de check-out "15/10/2024"
Then "Ana" é redirecionado para a tela de resultados

Scenario: O usuário "Ana" busca uma reserva sem disponibilidade
Given que "Ana" está na tela de busca
When "Ana" escreve a cidade "Recife" no campo de busca
And seleciona no botão de buscar
And seleciona a data de check-in "10/10/2024"
And seleciona a data de check-out "15/10/2024"
And seleciona o número de quartos "6"
Then "Ana" é redirecionado para a tela de resultados
And é exibida a mensagem "Não há disponibilidade para a data selecionada", com status code "404"
