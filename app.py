from flask import Flask, request, redirect, render_template, url_for, session, jsonify
import sett 
import services
import json
from users import users
from contacts import contatos




app = Flask(__name__)
app.secret_key = 'qualquer string serve'


@app.route('/', methods=['GET'])
def  inicio():
    print(session)
    if 'user' in session and 'password' in session:
        return realizar_login(session['user'], session['password'])

    return redirect(url_for('login'))

@app.route('/login', methods=['GET'])
def login():
    if 'user' in session and 'password' in session:
        return realizar_login(session['user'], session['password'])
    return render_template('login.html')

@app.route('/principal', methods=['GET', 'POST'])
def principal():
    if 'user' not in session or 'password' not in session:
        return redirect(url_for('login'))
    user = users[session['user']]
    print(session.get('person'))
    return render_template('principal.html', name=user['name'], picture="img/"+user['picture'],contatos=contatos, text=session.get('text', None))

@app.route('/authuser', methods=['POST'])
def authuser():
    user = request.form['user']
    password = request.form['password']

    return realizar_login(user, password)

def realizar_login(usuario, senha):
    # Verificar se o usuário existe no dicionário e se a senha está correta
    if usuario in users and users[usuario]['password'] == senha:
        print("Login bem-sucedido " + usuario)
        session['user'] = usuario
        session['password'] = senha
        return redirect(url_for('principal'))
    else:
        print("Usuário ou senha incorretos.")
        return redirect(url_for('login')+'?Error=NotAuthorized')


@app.route('/sendMessage', methods=['POST'])
def sendMessage():
    try:
        number = request.form.get('number')
        text = request.form.get('text')
        message = services.text_Mensagem(number, text)

        print("message = "+str(message))

        services.enviar_Mensagem_whatsapp(message)
        return 'OK'
    except Exception as e:
        return 'não enviado '+str(e)
    
@app.route('/fetchMessage', methods=['GET'])
def fetch_message():
    try:
         number = request.args.get('from')  # Obtém o número do remetente da solicitação GET.
         messageId = request.args.get('id')  # Obtém o ID da mensagem da solicitação GET.
         name = request.args.get('name')  # Obtém o nome do remetente da solicitação GET.

         if not all([number, messageId, name]):  # Verifica se todos os parâmetros necessários estão presentes.
             raise ValueError("Parâmetros incompletos")

         text = services.obtener_Mensagem_whatsapp(request.args)  # Passa toda a solicitação para a função de obtenção de mensagem.

         return jsonify({'message': str(text)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/webhook', methods=['GET'])
def verificar_token():
    try:
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token == sett.token:
            if challenge != None:
                return challenge
            else:
                return 'challenge nulo'
        else:
            return 'token incorreto', request.args.get('hub.verify_token')
    except Exception as e:
        return e,403

@app.route('/webhook', methods=['POST'])
def receber_mensagens():
    try:
        body = request.get_json()
        entry = body['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        message = value['messages'][0]
        number = message['from']
        messageId = message['id']
        contacts = value['contacts'][0]
        name = contacts['profile']['name']
        text = services.obtener_Mensagem_whatsapp(message)

        services.administrar_chatbot(text, number,messageId,name)
        
        
        return text

    except Exception as e:
        return 'não enviado ' + str(e)

if __name__ == '__main__':
    app.run()
