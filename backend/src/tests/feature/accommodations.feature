Feature: Create accommodations

    Creating the accommodations and posting them in the db

Scenario: Criar uma acomodação com um user_id existente
    Given existe um user com id "yasmin123" no banco de dados
    When uma requisição POST for enviada para "/accommodation/create" e adiciona-se os dados da acomodação nos campos: name: "Castelo RaTimBum", location: "Recife", bedrooms : "8", max_capacity: "16", description: "Divirta-se com as aventuras de Nino e seus amigos em um castelo mágico repleto de coisas curiosas.", user_id: "yasmin123"
    Then o status da resposta a ser mostrada é "200"
    And a resposta deve conter a mensagem "Accommodation created successfully!"

Scenario: Criar uma acomodação com um user_id inexistente
    Given não existe um user com id "lucinda456" no banco de dados
    When uma requisição de POST é requisitada para "/accommodation/create" e adiciona-se os dados da acomodação nos campos: name: "Castelo RaTimBum", location: "Recife", bedrooms : "8", max_capacity: "16", description: "Divirta-se com as aventuras de Nino e seus amigos em um castelo mágico repleto de coisas curiosas.", user_id: "lucinda456", price: "100"
    Then o status da resposta a ser mostrada é "400"
    And a resposta deve conter a mensagem "Invalid user ID."

Scenario: Criar uma acomodação com nome cujo tamanho é maior que 20 char
    Given existe um user com id "yasmin123" no banco de dados
    When uma requisição POST for enviada para "/accommodation/create" e adiciona-se os dados da acomodação nos campos: name: "Castelo da Barbie e o Quebra Nozes", location: "Recife", bedrooms : "8", max_capacity: "16", description: "Divirta-se com as aventuras de Barbie e seus amigos em um castelo mágico repleto de coisas curiosas.", user_id: "yasmin123", price: "100"
    Then o status da resposta a ser mostrada é "400"
    And a resposta deve conter a mensagem "Accommodation name must be 20 characters or less."

Scenario: Criar uma acomodação com zero quartos 
    Given existe um user com id "yasmin123" no banco de dados
    When uma requisição POST é enviada para "/accommodation/create" e adiciona-se os dados da acomodação nos campos: name: "Castelo da Barbie", location: "Recife", bedrooms : "0", max_capacity: "16", description: "Divirta-se com as aventuras de Barbie e seus amigos em um castelo mágico repleto de coisas curiosas.", user_id: "yasmin123", price: "100"
    Then o status da resposta a ser mostrada é "400"
    And a resposta deve conter a mensagem "Number of bedrooms must be a positive integer."

