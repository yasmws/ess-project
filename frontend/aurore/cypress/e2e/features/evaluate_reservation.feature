
Scenario: adicionando nova avaliação
Given eu estou logado com o usuário “Paulo”, email "paulo@gmail.com" e senha "123456"
And eu estou na página "Historic"
And eu fiz uma reserva no hotel “Dalhousie Castle” checkin no dia “23/09/2023” e checkout no dia "23/09/2023"
And clico em "avaliar" para a reserva no hotel “Dalhousie Castle” do dia “23/09/2023” e checkout no dia "23/09/2023"
When eu adiciono “5-estrelas” 
And eu seleciono a opção “enviar” 
Then vou para a pagina "Historic"
And eu posso ver na reserva do hotel “Dalhousie Castle” a avaliação “5 estrelas”
	
Scenario: adicionando nova avaliação mas não adicionando nenhuma estrela
Given eu estou logado com o usuário “Robert”, email "robert@gmail.com" e senha "123456"
And eu estou na página "Historic"
And eu fiz uma reserva no hotel “Cecil hotel” checkin no dia “23/09/2023” e checkout no dia "23/09/2023"
And clico em "avaliar" para a reserva no hotel  “Cecil hotel” checkin no dia “23/09/2023” e checkout no dia "23/09/2023"
When eu não adiciono nenhuma “estrela” 
And eu adiciono “terrivel” no campo de comentário
And eu seleciono a opção “enviar” 
Then eu ainda estou na pagina "avaliação"
And a avaliação não envia

Scenario: tento mudar uma avaliação minha
Given eu estou logado com o usuário “Sara”, email "robert@gmail.com" e senha "123456"
And eu estou na página "Historic"
And eu fiz uma avaliação para a reserva no hotel “Ahwahnee Hotel” checkin no dia “23/09/2023” e checkout no dia "23/09/2023"
When clico em "avaliar" para a reserva no hotel “Ahwahnee Hotel” do dia “30/02/2023”
Then eu estou na página "Historic"
