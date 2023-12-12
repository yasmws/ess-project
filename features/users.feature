Feature: gerenciamento de reserva
	as a usuário misto
	i want to poder reservar, editar e excluir reservas 
           So ficará certificado que estou em um sistema funcional e que atenda os requisitos mínimos


Scenario: Histórico de reserva como como cliente

 Given estou logado com o login "YVSO" e senha "@56337", na página “MINHAS RESERVAS”
     When  seleciono a opção de “HISTÓRICO” 
     Then é me listado uma reserva com os dados  “TIPO”, “CIDADE”, “ESATADIA”
     and “TIPO”, “CIDADE”, “ESATADIA” está preenchido por “small room”, “Japão”, “14/02/24 a 17/02/24”


Scenario: Visualizar lista de ofertas como servidor

     Given estou logado com o login "YVSO" e senha "@56337", na página “ADMINISTRAR RESERVA”
     When seleciono a opção “OFERTAS” 
     Then é me listado uma reservaa em aberto com as descrições “Kitnet 2 pessoas”, “casa na praia 3 quartos, 1 suíte” 


Scenario: Editar detalhes de oferta 

	Givenestou logado com o login "YVSO" e senha "@56337" na tela de “ADMINISTRAR RESERVA OFERTADA”
	And existe uma oferta reservada para “Kaylane Gonçalves Lira”, com e-mail “kgl@cin.ufpe.br” para os dias “21/03/24” e “21/03/24” 
     And informações “TIPO DE HOSPEDAGEM”, “PESSOAS”, “ANIMAIS”, “AR-CONDICIONADO”, os quais são preenchidos por “Casa de Praia”, “até 6 pessoas”, “Não”, “Sim”.
     When seleciono a opção de "editar"
     And eu preencho o campo “ANIMAL”  com “Sim”
     Then uma mensagem de confirmação é mostrada na tela: “Edição adicionada com sucesso”.


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
     
Scenario: Cancelar reserva de cliente 

        Given que estou logado com o login "YVSO" e senha "@56337" na tela  “ADMINISTRAR RESERVA OFERTADA”
        And existe uma oferta reservada para “Kaylane Gonçalves Lira”, com e-mail “kgl@cin.ufpe.br” para os dias “21/03/24” e “21/03/24”
        When eu excluo a reserva e seleciono a opção “cancelar reserva”
        And uma tela com campos  a preencher aparece
        And seleciona o campo “RUDE” no campo “comportamento do cliente”
        And preencho o campo obrigatório de comentário com o seguinte texto: ” Kaylane Gonçalvez foi muito rude em nosso primeiro encontro” 
        And seleciono em “confirmar”
        Then uma tela de confirmação com a informação “Reserva cancelada” aparece na tela 
        And a oferta aparece no sistema para ser ofertada a outros interessados

Scenario: Cancelar reserva existente com cobrança de juros

     Given estou logado com o login "YVSO" e senha "@56337" na página “MINHAS RESERVAS” 
     And existe uma vada de datas de “check in” e “check out, sendo respectivamente para os dias entre “17/01/2024” e “25/01/2024”
     When eu clico no botão de “CANCELAR RESERVA”
	And uma tela com a frase “Cancelar reserva para os dias entre “17/01/2024” e “25/01/2024”?”
	And eu seleciono “Confirmar”
     And  retorno para a tela “MINHAS RESERVAS” 
	Then eu vejo a seguinte mensagem “Nenhuma reserva no seu nome”
     
