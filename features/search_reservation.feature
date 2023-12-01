Feature: Busca de Reservas

Scenario: O usuário busca uma reserva pela localização
Given que o usuário está na tela de busca
When o usuário escreve a cidade "Recife" no campo de busca
And clica no botão de buscar
Then o usuário é redirecionado para a tela de resultados

Scenario: O usuário busca uma reserva pelo nome do hotel
Given que o usuário está na tela de busca
When o usuário escreve o nome do hotel "Hotel Boa viagem" no campo de busca
And clica no botão de buscar
Then o usuário é redirecionado para a tela de resultados

Scenario: O usuário busca uma reserva pela localização com filtro de data
Given que o usuário está na tela de busca
When o usuário escreve a cidade "Recife" no campo de busca
And clica no botão de buscar
And seleciona a data de check-in "10/10/2024"
And seleciona a data de check-out "15/10/2024"
Then o usuário é redirecionado para a tela de resultados

Scenario: O usuário busca uma reserva sem disponibilidade
Given que o usuário está na tela de busca
When o usuário escreve a cidade "Recife" no campo de busca
And seleciona no botão de buscar
And seleciona a data de check-in "10/10/2024"
And seleciona a data de check-out "15/10/2024"
And seleciona o número de quartos "6"
Then o usuário é redirecionado para a tela de resultados
And é exibida a mensagem "Não há disponibilidade para a data selecionada", com status "404"
