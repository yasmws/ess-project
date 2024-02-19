Feature: Cadastrar forma de pagamento

    As a usuário
    I want to cadastrar formas de pagamento
    so that eu posso adicionar formas de pagamento ao meu perfil

    Scenario: Cadastrar forma de pagamento (limite não atingido)
        Given o sistema possui um registro de usuário com username "henrique" e valor de cnt menor que 3
        When uma requisição "POST" for enviada para "/payment/add" com tipo "boleto" e id "None"
        Then o status da resposta deve ser "200"
        And o JSON de resposta deve ter tipo "boleto" e id "None"