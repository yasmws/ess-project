Feature: Teste da Página de Busca

Scenario: Verificar se a página de busca está funcionando corretamente
  Given Eu estou na página de busca
  When Eu preencho o formulário de busca
  And Eu clico no botão de busca
  Then Eu vejo os resultados da busca
