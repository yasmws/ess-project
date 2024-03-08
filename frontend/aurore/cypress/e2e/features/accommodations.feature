Feature: Criar e visualizar item
  As a usuário
  I want criar e visualizar meus item criados.
  so that eu possa ter um histórico de item.

Scenario: Criar um item
  Given o usuário está na página ""
  When o usuário preenche o campo "item-input" com "Eda, the Owl Lady"
  And o usuário escolhe a opção "create-item"
  Then o usuário vê a mensagem "Item criado com sucesso!"

Scenario: Visualizar item
  Given o usuário está na página ""
  When o usuário escolhe a opção "view-items"
  Then o usuário está na página "items"
  And o usuário visualiza o item "792" de nome "Naruto com chapéu do Luffy"