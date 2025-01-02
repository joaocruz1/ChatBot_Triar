# Sistema de ChatBot - ChatHub 🤖

Bem-vindo ao repositório do **ChatHub**, um sistema de chatbot para comunicação via WhatsApp. Este projeto foi desenvolvido usando Flask e integra o envio e recebimento de mensagens no WhatsApp através da API do WhatsApp Business.

## Descrição 📜

O **ChatHub** é um sistema de chatbot que permite interagir com os usuários através do WhatsApp. O sistema recebe mensagens de clientes e responde com base em um conjunto de regras, como fornecer informações de contato ou direcionar o usuário para departamentos específicos. O sistema também pode responder interativamente com botões e opções de lista.

## Tecnologias Utilizadas 🛠️

Este projeto foi desenvolvido com as seguintes tecnologias:

- **Flask**: Framework web para Python para criar e gerenciar rotas e comunicação do servidor.
- **JavaScript/jQuery**: Usado para atualizar a interface de forma dinâmica e enviar as mensagens via AJAX.
- **WhatsApp API**: Para enviar e receber mensagens no WhatsApp.
- **HTML e CSS**: Para a interface de usuário do sistema.

## Funcionalidades ✨

- **Login de Usuário 🔐**: Sistema de autenticação com senha para acessar o painel principal.
- **Interação com ChatBot 🤖**: O ChatBot pode responder a perguntas e direcionar para diferentes departamentos (Exemplo: Recepção, RH, Financeiro, etc.).
- **Envio e Recebimento de Mensagens 📲**: Integração com a API do WhatsApp para envio e recebimento de mensagens.
- **Respostas Interativas 💬**: Respostas com botões de interação e listas de opções para o usuário.
- **Gerenciamento de Conversas 💼**: O sistema permite a comunicação com vários contatos ao mesmo tempo, com troca de mensagens dinâmica.

## Funcionalidades Adicionais 🔧

- **Resposta automática com botões de opções 🔘**: O sistema permite ao usuário escolher entre várias opções de departamentos e serviços.
- **Gerenciamento de mensagens 📝**: O sistema identifica o tipo de mensagem (texto, botão, lista) e responde adequadamente.
- **Sistema de autenticação 🔑**: Apenas usuários autenticados têm acesso ao painel de controle.

## Como Rodar o Projeto 🚀

1. **Clone o Repositório**:

```bash
git clone https://github.com/seu-usuario/chathub.git
Instale as Dependências 📦: Certifique-se de ter o Python 3.x instalado. Para instalar as dependências, use o seguinte comando:
bash
Copy code
pip install -r requirements.txt
Configuração do WhatsApp API 📱: Você precisará de uma conta do WhatsApp Business e configurar o token de autenticação e o URL da API. As credenciais podem ser definidas no arquivo sett.py.

Inicie o Servidor 🖥️: Execute o servidor Flask:

bash
Copy code
python app.py
O servidor estará disponível em http://127.0.0.1:5000/ por padrão.

Endpoints da API 🌐
/: Página inicial que verifica o status de login.
/login: Página de login para usuários.
/principal: Página principal para usuários autenticados, onde podem interagir com os contatos.
/authuser: Endpoint de autenticação para verificar as credenciais do usuário.
/sendMessage: Envia uma mensagem para o número do cliente no WhatsApp.
/webhook: Recebe mensagens e atualizações de status da API do WhatsApp.
Como Funciona 🛠️
Login de Usuário 🔑: O sistema verifica as credenciais do usuário, e se forem válidas, redireciona para a página principal.
Interação com o ChatBot 🤖: Quando um usuário envia uma mensagem, o ChatBot analisa o conteúdo e responde com uma série de opções interativas.
Envio de Mensagens 📲: O usuário pode enviar mensagens para os contatos selecionados, que são processadas pela API do WhatsApp.
Recebimento de Mensagens 💬: O sistema captura as mensagens recebidas do WhatsApp e as processa de acordo com as regras do ChatBot.
Contribuições 🎉
Se você deseja contribuir para este projeto, por favor siga as etapas abaixo:

Faça um fork deste repositório.
Crie uma nova branch (git checkout -b feature-nome).
Faça suas alterações e commit (git commit -am 'Adiciona nova funcionalidade').
Push para a branch (git push origin feature-nome).
Abra um Pull Request.
Licença 📄
Este projeto está sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato 📬
Se você tiver dúvidas ou sugestões sobre o sistema, fique à vontade para entrar em contato via:

Instagram: @joaovcruz1
E-mail: joao.cruz@example.com
