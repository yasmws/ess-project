Feature: Deletar forma de pagamento

    As a usuário 
    I want to deletar formas de pagamento
    so that eu posso remover formas de pagamento cadastradas

    Scenario: Deletar forma de pagamento (operação sucedida)
	    Given eu estou logado como usuário de nome "Henrique", email "eurico@tomail.com" e senha "3ur1c0"
		And eu estou na página "Formas de pagamento"
	    And eu vejo a forma de pagamento "Cascalho" de número/código "123456-789" listada no perfil
	    When eu seleciono "Remover forma de pagamento"
	    And eu seleciono "Confirmar"
	    Then eu consigo ver uma mensagem de confirmação "Forma de pagamento removida"
	    And eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema sem formas de pagamento cadastradas
	    And eu consigo ver "Nenhuma forma de pagamento cadastrada" no perfil 

    Scenario: Deletar forma de pagamento (operação cancelada)
	    Given eu estou logado como usuário de nome "Henrique", email "eurico@tomail.com" e senha "3ur1c0"
		And eu estou na página "Formas de pagamento"
	    And eu vejo a forma de pagamento "Cascalho" de número/código "123456-789" listada no perfil
	    When eu seleciono "Remover forma de pagamento"
	    And eu seleciono "Cancelar"
	    Then eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com a forma de pagamento "Cascalho" de número/código "123456-789" cadastrada
	    And eu consigo ver a forma de pagamento "Cascalho" com número/código "123456-789" listada no perfil
