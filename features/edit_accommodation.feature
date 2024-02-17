
 --- GUI 
 
Feature: gerenciamento de reserva
	as a usuário misto
	i want to poder editar, excluir reservas 
    So atendo os requisitos de geremciamento de reserva

Caso tenha comprador:

-- Após comprada só pode ser editado capacidade_max caso não tenha ocupado tal limite
-- descrição pode
-- Não pode nome
-- Não pode localização
-- banheiros não


Scenario: Editar detalhes de acomodação já reservada

	Given estou logado com o email "yvso@cin.ufpe.br" e senha "@56337" na tela “ACOMODAÇÕES”
	And existe uma acomodação com o nome "Vovó pequena", localização "Gravatá", descrição "Um chalé requintado", banheiros "3", capacidade máxima "100" 
    And está reservada para “Kaylane Gonçalves Lira”, com e-mail “kgl@cin.ufpe.br” e id "7172712712172" para os dias “21/03/24” e “27/03/24” 
    When seleciono a opção de "editar"
    And eu preencho o campo “capacidade máxima”  com “80”
    Then uma mensagem de confirmação é mostrada na tela: “Edição adicionada com sucesso”.
    And um email é mandado atomaticamente para “kgl@cin.ufpe.br” com a informação "Vovó Pequena auterou capacidade máxima para 80"
    And a acomodação com o nome "Vovó pequena" agora registra capacidade máxima "80"

Scenario: Editar detalhes de acomodação não reservado

	Given estou logado com o email "yvso@cin.ufpe.br" e senha "@56337" na tela “ACOMODAÇÕES”
	And existe uma acomodação com o nome "Vovó pequena", localização "Gravatá", descrição "Um chalé requintado", banheiros "3", capacidade máxima "100" 
    When seleciono a opção de "editar"
    And eu preencho o campo “localização”  com “Caruaru” e "banheiros" com "5"
    Then uma mensagem de confirmação é mostrada na tela: “Edição adicionada com sucesso”.
    And a acomodação com o nome "Vovó pequena" agora registra localização "Caruaru" e "5" banheiros.

Scenario: Editar acomodação desconsiderando campo obrigatório

    Given estou logado com o email "yvso@cin.ufpe.br" e senha "@56337" na tela “ACOMODAÇÕES”
	And existe uma acomodação com o nome "Vovó pequena", localização "Gravatá", descrição "Um chalé requintado", banheiros "3", capacidade máxima "100" 
    When seleciono a opção de "editar"
    And eu preencho o campo "banheiros" com "5" “localização” deixo em branco
    Then uma mensagem de alerta é mostrada na tela: “Falha ao editar acomodação”.


Scenario: Editar capacidade máxima com limite atingido

    Given estou logado com o email "yvso@cin.ufpe.br" e senha "@56337" na tela “ACOMODAÇÕES”
	And existe uma acomodação com o nome "Vovó pequena", localização "Gravatá", descrição "Um chalé requintado", banheiros "3", capacidade máxima "100" 
    And a quantidade de reservas já atingiu o limite de capacidade máxima
    When seleciono a opção de "editar"
    And eu preencho o campo "capacidade_max" com "80"
    Then uma mensagem de alerta é mostrada na tela: “Falha ao editar. Capacidade máxima atingida”.
    



