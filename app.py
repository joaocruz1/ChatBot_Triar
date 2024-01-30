from flask import Flask, request, redirect, render_template, url_for, session
import sett 
import services
import json
from users import users

app = Flask(__name__)

@app.route('/', methods=['GET'])
def  inicio():
    return 'Pagina inicial teste'


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/principal', methods=['GET', 'POST'])
def principal():
    return render_template('principal.html')

@app.route('/authuser', methods=['POST'])
def authuser():
    user = request.form['user']
    password = request.form['password']

    login = realizar_login(user, password)

    if login:
        return redirect(url_for('principal'))
    else:
        return redirect(url_for('login')+'?Error=NotAuthorized')

def realizar_login(usuario, senha):
    # Verificar se o usuário existe no dicionário e se a senha está correta
    if usuario in users and users[usuario]['password'] == senha:
        print("Login bem-sucedido " + usuario)
        return True
    else:
        print("Usuário ou senha incorretos.")
        return False


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
        return 'enviado'

    except Exception as e:
        return 'no enviado ' + str(e)

if __name__ == '__main__':
    app.run()