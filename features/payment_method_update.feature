Feature: Atualizar formas de pagamento

    As a usuário 
    I want to atualizar formas de pagamento 
    so that eu posso alterar dados de formas de pagamento cadastradas 

    Scenario: Atualizar forma de pagamento
	    Given eu estou logado como usuário "Henrique"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo a forma de pagamento "Cascalho" de número/código "123456-789" listada no perfil
        When eu seleciono "Editar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "342516-978"
	    And eu seleciono "Confirmar"
	    Then eu consigo ver uma mensagem de confirmação da atualização da forma de pagamento
	    And eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com a forma de pagamento "Cascalho" de número/código "342516-978" cadastrada
	    And eu consigo ver a forma de pagamento "Cascalho" com número/código "342516-978" listada no perfil

    Scenario: Cancelar atualização de forma de pagamento
	    Given eu estou logado como usuário "Henrique"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo a forma de pagamento "Cascalho" de número/código "123456-789" listada no perfil
        When eu seleciono "Editar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "342516-978"
	    And eu seleciono "Cancelar"
	    Then eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com a forma de pagamento "Cascalho" de número/código "123456-789" cadastrada
	    And eu consigo ver a forma de pagamento "Cascalho" com número/código "123456-789" listada no perfil

