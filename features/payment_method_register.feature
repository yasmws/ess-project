Feature: Cadastrar forma de pagamento

    As a usuário
    I want to cadastrar formas de pagamento
    so that eu posso adicionar formas de pagamento ao meu perfil

    Scenario: cadastrar forma de pagamento (limite de formas de pagamento não atingido)
	    Given eu estou logado como usuário "Henrique"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo que não há formas de pagamento listadas no perfil
	    When eu seleciono "Adicionar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "XXXXXX-XXX"
	    And eu seleciono "Confirmar"
	    Then eu consigo ver uma mensagem de confirmação do cadastro da nova forma de pagamento
	    And eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com a forma de pagamento "Cascalho" de número/código "XXXXXX-XXX" cadastrada
	    And eu consigo ver a forma de pagamento "Cascalho" com número/código "XXXXXX-XXX" listada no perfil

    Scenario: cadastrar forma de pagamento (limite de formas de pagamento atingido)
	    Given eu estou logado como usuário "Henrique"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo as formas de pagamento "Sal, Papel, Moeda" listadas no perfil
	    When eu seleciono "Adicionar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "XXXXXX-XXX"
	    And eu seleciono "Confirmar"
	    Then eu consigo ver uma mensagem de erro sobre limite de formas de pagamento atingido
	    And eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com as formas de pagamento "Sal, Papel, Moeda"
	    And eu consigo ver as formas de pagamento "Sal, Papel, Moeda" listadas no perfil

    Scenario: cadastrar forma de pagamento já cadastrada
	    Given eu estou logado como usuário "Henrique"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo a forma de pagamento "Cascalho" com número/código "XXXXXX-XXX" listada no perfil
	    When eu seleciono "Adicionar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "XXXXXX-XXX"
	    And eu seleciono "Confirmar"
	    Then eu consigo ver uma mensagem de erro sobre forma de pagamento já cadastrada
	    And eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com a forma de pagamento "Cascalho"
	    And eu consigo ver a forma de pagamento "Cascalho" listada apenas uma vez no perfil

    Scenario: cancelar cadastro de forma de pagamento
	    Given eu estou logado como usuário "Henrique"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo que não há formas de pagamento listadas no perfil
	    When eu seleciono "Adicionar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "XXXXXX-XXX"
	    And eu seleciono "Cancelar"
	    Then eu continuo na página "Formas de pagamento"
	    And o perfil de usuário "Henrique" é registrado no sistema com a forma de pagamento "Cascalho"
	    And eu consigo ver que não há formas de pagamento listadas no perfil

    Scenario: cadastrar de forma de pagamento inválida
	    Given eu estou logado como usuário "Henrique"
	    And eu estou na página "Formas de pagamento"
	    And eu vejo que não há formas de pagamento listadas no perfil
	    When eu seleciono "Adicionar forma de pagamento"
	    And eu preencho os dados com tipo "Cascalho" e número/código "---"
	    And eu seleciono "Confirmar"
	    Then eu consigo ver uma mensagem de erro sobre forma de pagamento inválida
        And eu continuo na página "Formas de pagamento"
        And eu consigo ver que não há formas de pagamento listadas
        