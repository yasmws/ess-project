
Scenario: Histórico de reserva como como cliente

 Given eu estou logado, na funcionalidade de usuário, na página “MINHAS RESERVAS”
     When  eu vejo o campo “HISTÓRICO” e o seleciono 
     Then é me listado uma reserva com os seguintes dados  “TIPO”, “CIDADE”, “ESATADIA”:   “small room”, “Japão”, “14/02/24 a 17/02/24” 


Scenario: Visualizar lista de ofertas como servidor

     Given eu estou logado, na funcionalidade de administrador, na página “ADMINISTRAR RESERVA”

     When eu vejo o campo “RESERVA ABERTA”  e o seleciono
     Then é me listado as reservas com os discriminantes  “Kitnet 2 pessoas”, “casa na praia 3 quartos, 1 suíte” que ainda não foram reservadas


Scenario: Editar detalhes de oferta 

	Given que estou logado  na tela de “ADMINISTRAR RESERVA OFERTADA”
	And existe uma oferta reservada para “Kaylane Gonçalves Lira”, com e-mail “kgl@cin.ufpe.br” para os dias “21/03/24” e “21/03/24” 
          And informações de oferta  “TIPO DE HOSPEDAGEM”, “PESSOAS”, “ANIMAIS”, “AR-CONDICIONADO”, os quais são preenchidos respectivamente por “Casa de Praia”, “até 6 pessoas”, “Não”, “Sim”.

When seleciono a opção de editar
And eu preencho o campo “ANIMAL”  com “Sim”
    	Then uma mensagem de confirmação é mostrada na tela, sendo a mensagem: “Edição adicionada com sucesso”.


Scenario: Editar dias de reservas como usuário comum

	Given estou logado na página “RESERVAR ESTADIA” 
          And no board “RESERVA” as minhas datas de “check in” e “check out” marcadas de “CINZA”,  sendo respectivamente os dias “17/01/2024” e “25/01/2024”, custeando no campo “VALOR” 1450,0 R$ são mostradas
           When seleciono  o botão “EDITAR RESERVA”
	And seleciono os dias entre “15/01/2024”  e “20/01/2024” que estão “AZUL”, ou seja, disponíveis para reserva
       AND eu seleciono “CONFIRMAR”
         Then uma tela de atualização “NOVAS DATAS INSERIDAS COM SUCESSO” aparece para mim
	And eu consigo ver no board ilustrativo  “RESERVA” as minhas datas de “check in” e “check out” marcadas de “CINZA”,  sendo respectivamente o intervalo de  dias entre “15/01/2024” e “20/01/2024”, custeando no campo “VALOR” 967,0 R$.



Scenario: Cancelar reserva de cliente 

        Given que estou logado na tela  “ADMINISTRAR RESERVA OFERTADA”
        And existe uma oferta reservada para “Kaylane Gonçalves Lira”, com e-mail “kgl@cin.ufpe.br” para os dias “21/03/24” e “21/03/24”
        When eu excluo a reserva e seleciono o em “cancelar reserva”
        AND uma tela com campos  a preencher sobre o cancelamento aparece
        AND seleciona o campo “RUDE” no campo “comportamento do cliente”
        AND preencho o campo obrigatório de comentário com o seguinte texto: ” Kaylane Gonçalvez foi muito rude em nosso primeiro encontro” 
        AND seleciono em “confirmar”

        Then uma tela de confirmação com a informação “Reserva cancelada” aparece na tela 

        AND a oferta aparece no sistema para ser ofertada a outros interessados

Scenario: Cancelar reserva existente com cobrança de juros

 Given estou logado na página “MINHAS RESERVAS” onde encontro minhas datas de “check in” e “check out, sendo respectivamente os dias entre “17/01/2024” e “25/01/2024”, as quais reservei faz dois.
	When eu clico no botão de “CANCELAR RESERVA”
	 And uma tela de Span com a frase “Cancelar reserva para os dias entre “17/01/2024” e “25/01/2024”?”
	And eu seleciono “Confirmar”
            And  retorno para a tela “MINHAS RESERVAS” 
	Then eu vejo a seguinte mensagem “Nenhuma reserva no seu nome” e abaixo dessa mensagem um “RELATÓRIO FINANCEIRO” registrando o reenbolso com juros de 20% por cancelamento após 1 dia últil .
           
