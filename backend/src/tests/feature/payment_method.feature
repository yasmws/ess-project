Feature: Cadastrar forma de pagamento

    As a usuário
    I want to cadastrar formas de pagamento
    so that eu posso adicionar formas de pagamento ao meu perfil

    Scenario: Cadastrar forma de pagamento (limite não atingido)
        Given o sistema possui um registro de usuário com username "rafa" e valor de cnt menor que 3
        When uma requisição "POST" for enviada para "/payment/add" com tipo "boleto" e id "None"
        Then o status da resposta deve ser "200"
        And o JSON de resposta deve ter tipo "boleto" e id "None"

    Scenario: Cadastrar forma de pagamento (limite atingido)
        Given o sistema possui um registro de usuário com username "pedro123" e valor de cnt igual a 3
        When uma requisição "POST" for enviada para "/payment/add" com tipo "debito" e id "1346 7908 7542 1346"
        Then o status da resposta deve ser "400"
        And o JSON de resposta deve ter a mensagem "Limite de formas de pagamento atingido!"

    Scenario: Cadastrar forma de pagamento já cadastrada
        Given o sistema possui um registro de usuário com username "yasmimvso"
        And "yasmimvso" possui um registro de forma de pagamento com tipo "pix" e id "None"
        When uma requisição "POST" for enviada para "/payment/add" com tipo "pix" e id "None"
        Then o status da resposta deve ser "409"
        And o JSON de resposta deve ter a mensagem "Essa forma de pagamento ja esta registrada!"

    Scenario: Atualizar forma de pagamento
        Given o sistema possui um registro de usuário com username "rafaael"
        And "rafaael" possui um registro de forma de pagamento com tipo "credito" e id "3465 7652 7326 2347"
        When uma requisição "PUT" for enviada para "/payment/update" com tipo "pix" e id "None"
        Then o status da resposta deve ser "200"
        And o JSON de resposta deve ter tipo "pix" e id "None"

    Scenario: Tentar atualizar dados inválidos
        Given o sistema possui um registro de usuário com username "saran"
        And "saran" possui um registro de forma de pagamento com tipo "debito" e id "7256 1528 97 0246"
        When uma requisição "PUT" for enviada para "/payment/update" com tipo "debito" e id "None"
        Then o status da resposta deve ser "400"
        And o JSON de resposta deve ter a mensagem "Numero de id informado nao eh valido!"

    Scenario: Deletar forma de pagamento (operação sucedida)
        Given o sistema possui um registro de usuário com username "yoni"
        And "yoni" possui um registro de forma de pagamento com tipo "pix" e id "None"
        When uma requisição "DELETE" for enviada para "/payment/delete"
        Then o status da resposta deve ser "200"
