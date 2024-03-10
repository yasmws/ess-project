Feature: Cadastrar forma de pagamento

    As a usuário
    I want to cadastrar formas de pagamento
    so that eu posso adicionar formas de pagamento ao meu perfil

    Scenario: Cadastrar forma de pagamento (limite não atingido)
        Given o sistema possui um registro de usuário com username "rafaael" e valor de cnt menor que 3
        When uma requisição POST for enviada para "/payment/rafaael/add" com tipo "pix" e id "None"
        Then o status da resposta deve ser "200"
        And o JSON de resposta deve ter a mensagem "Payment method added!"

    Scenario: Cadastrar forma de pagamento (limite atingido)
        Given o sistema possui um registro de usuário com username "rafa" e valor de cnt igual a 3
        When uma requisição POST for enviada para "/payment/rafa/add" com tipo "debito" e id "1346 7908 7542 1346"
        Then o status da resposta deve ser "400"
        And o JSON de resposta deve ter a mensagem "Payment methods' limit reached!"

    Scenario: Cadastrar forma de pagamento já cadastrada
        Given o sistema possui um registro de usuário com username "rafaael"
        And "rafaael" possui um registro de forma de pagamento com tipo "pix" e id "None"
        When uma requisição POST for enviada para "/payment/rafaael/add" com tipo "pix" e id "None"
        Then o status da resposta deve ser "409"
        And o JSON de resposta deve ter a mensagem "This payment method is already registered!"

    Scenario: Atualizar forma de pagamento
        Given o sistema possui um registro de usuário com username "rafaael"
        And "rafaael" possui uma forma de pagamento cadastrada sob o referencial "method1" 
        When uma requisição PUT for enviada para "/payment/rafaael/update" referente a forma de pagamento com tipo "credito" e id "3455 7652 7326 2347"
        Then o status da resposta deve ser "200"
        And o JSON de resposta deve ter a mensagem "Payment method updated!"

    Scenario: Tentar atualizar dados inválidos
        Given o sistema possui um registro de usuário com username "rafa"
        And "rafa" possui uma forma de pagamento cadastrada sob o referencial "method1" 
        When uma requisição PUT for enviada para "/payment/rafa/update" referente a forma de pagamento com tipo "credito" e id "None"
        Then o status da resposta deve ser "400"
        And o JSON de resposta deve ter a mensagem "This payment method demands an id number."

    Scenario: Deletar forma de pagamento (operação sucedida)
        Given o sistema possui um registro de usuário com username "rafaael"
        And "rafaael" possui uma forma de pagamento cadastrada sob o referencial "method1" 
        When uma requisição DELETE for enviada para "/payment/rafaael/delete" referente a essa forma de pagamento
        Then o status da resposta deve ser "200"
        And o JSON de resposta deve ter a mensagem "Payment method deleted!"
