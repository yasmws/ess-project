Feature: gerenciamento de reserva
	as a usuário misto
	i want to poder editar, excluir reservas 
     So ficará certificado que estou em um sistema funcional e que atenda os requisitos mínimos


Scenario: Histórico de reserva 

    Given estou logado com o login "YVSO" e senha "@56337"
    And estou na página “MINHAS RESERVAS”
    When  seleciono a opção de “HISTÓRICO” 
    Then é me listado uma reserva com os dados  “TIPO”, “CIDADE”, “ESATADIA”
    And “TIPO”, “CIDADE”, “ESATADIA” estão preenchidos respectivamente com “small room”, “Japão”, “14/02/24 a 17/02/24”


Scenario: Visualizar lista de ofertas como servidor

     Given estou logado com o login "YVSO" e senha "@56337"
     And estou na página “ADMINISTRAR RESERVA”
     When seleciono a opção “OFERTAS” 
     Then é me listado uma reservaa em aberto com as descrições “Kitnet 2 pessoas”, “casa na praia 3 quartos, 1 suíte” 


Scenario: Editar dias de reservas como usuário comum

	Given estou logado com o login "YVSO" e senha "@56337" na página “RESERVAR ESTADIA” 
     And na opção de “RESERVA” existe uma reserva com a data de “check in” e “check out” respectivamente para os dias “17/01/2024” e “25/01/2024”
     And a reserva está custeando no campo “VALOR” 1450,0 R$
     When seleciono  o botão “EDITAR RESERVA”
	And seleciono os dias entre “15/01/2024”  e “20/01/2024”, que estão disponíveis para reserva
     And seleciono “CONFIRMAR”
     Then uma tela de atualização “NOVAS DATAS INSERIDAS COM SUCESSO” aparecem como mensagem
	And as datas de “check in” e “check out” são respectivamente o intervalo de  dias entre “15/01/2024” e “20/01/2024”
     And essa nova reserva está custeando no campo “VALOR”,  967,0 R$.
     
Scenario: Cancelar reserva 

        Given que estou logado com o login "YVSO" e senha "@56337"
        And estou na tela  “ADMINISTRAR RESERVA OFERTADA”
        And existe uma oferta reservada para “Kaylane Gonçalves Lira”, com e-mail “kgl@cin.ufpe.br” para os dias “21/03/24” e “21/03/24”
        When seleciono a opção “cancelar reserva”
        And seleciona o campo “RUDE” no campo “comportamento do cliente”
        And preencho o campo de comentário com "Kaylane Gonçalvez foi muito rude em nosso primeiro encontro” 
        And seleciono em “confirmar”
        Then uma tela de confirmação com a informação “Reserva cancelada” aparece na tela 
        And retorno para a tela  “ADMINISTRAR RESERVA OFERTADA”

Scenario: Cancelar reserva existente com cobrança de juros

     Given estou logado com o login "YVSO" e senha "@56337" na página “MINHAS RESERVAS” 
     And existe uma vada de datas de “check in” e “check out, sendo respectivamente para os dias entre “17/01/2024” e “25/01/2024”
     When eu clico no botão de “CANCELAR RESERVA”
	And uma tela com a frase “Cancelar reserva para os dias entre “17/01/2024” e “25/01/2024”?”
	And eu seleciono “Confirmar”
     And  retorno para a tela “MINHAS RESERVAS” 
	Then eu vejo a seguinte mensagem “Nenhuma reserva no seu nome”
     
