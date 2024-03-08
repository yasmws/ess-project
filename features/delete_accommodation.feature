Feature: gerenciamento de reserva
	as a usuário misto
	i want to poder editar, excluir reservas 
    So atendo os requisitos de geremciamento de reserva


-- Excluir sem reservas
-- Excluir com reservas

Scenario: Excluir acomodação existente sem reserva

Given estou logado com o email "yvso@cin.ufpe.br" e senha "@56337" na tela “ACOMODAÇÕES”
	And existe uma acomodação com o nome "Vovó pequena", localização "Gravatá", descrição "Um chalé requintado", banheiros "3", capacidade máxima "100" 
    When seleciono a opção de "excluir"
    Then uma mensagem de confirmação é mostrada na tela: “Acomodação com sucesso”.
    And a acomodação com o nome "Vovó pequena" agora não está mais registrada na tela “ACOMODAÇÕES”.

Scenario: Excluir acomodação existente com reserva