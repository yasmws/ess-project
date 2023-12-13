Feature: Atualizar formas de pagamento

    As a usuário 
    I want to atualizar formas de pagamento 
    so that eu posso alterar dados de formas de pagamento cadastradas 

    Scenario: Atualizar forma de pagamento
	    Given eu estou logado como usuário de nome "Henrique", email "eurico@tomail.com" e senha "3ur1c0"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo a forma de pagamento "Cascalho" de número/código "123456-789" listada no perfil
        When eu seleciono "Editar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "342516-978"
	    And eu seleciono "Confirmar"
	    Then eu consigo ver uma mensagem de confirmação "Forma de pagamento atualizada"
	    And eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com a forma de pagamento "Cascalho" de número/código "342516-978" cadastrada
	    And eu consigo ver a forma de pagamento "Cascalho" com número/código "342516-978" listada no perfil

    Scenario: Cancelar atualização de forma de pagamento
	    Given eu estou logado como usuário de nome "Henrique", email "eurico@tomail.com" e senha "3ur1c0"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo a forma de pagamento "Cascalho" de número/código "123456-789" listada no perfil
        When eu seleciono "Editar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "342516-978"
	    And eu seleciono "Cancelar"
	    Then eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com a forma de pagamento "Cascalho" de número/código "123456-789" cadastrada
	    And eu consigo ver a forma de pagamento "Cascalho" com número/código "123456-789" listada no perfil

    Scenario: Tentar atualizar dados inválidos
	    Given eu estou logado como usuário de nome "Henrique", email "eurico@tomail.com" e senha "3ur1c0"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo a forma de pagamento "Cascalho" de número/código "123456-789" listada no perfil
        When eu seleciono "Editar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "---"
	    And eu seleciono "Confirmar"
	    Then eu consigo ver uma mensagem de erro "Forma de pagamento inválida"
	    And eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com a forma de pagamento "Cascalho" de número/código "123456-789" cadastrada
	    And eu consigo ver a forma de pagamento "Cascalho" com número/código "123456-789" listada no perfil

    Scenario: Tentar atualizar com dados já cadastrados
	    Given eu estou logado como usuário de nome "Henrique", email "eurico@tomail.com" e senha "3ur1c0"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo as formas de pagamento "Cascalho" com número/código "372585-686" e "Papel" com número/código "123456-789" listadas no perfil
	    When eu seleciono "Editar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "372585-686"
	    And eu seleciono "Confirmar"
	    Then eu consigo ver uma mensagem de erro "Forma de pagamento já cadastrada"
	    And eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com as formas de pagamento "Cascalho" com número/código "372585-686" e "Papel" com número/código "123456-789"
	    And eu consigo ver as formas de pagamento "Cascalho" com número/código "372585-686" e "Papel" com número/código "123456-789" listadas no perfil
