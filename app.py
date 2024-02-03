from flask import Flask, request, redirect, render_template, url_for, session
import sett 
import services
import json
from users import users

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
    return render_template('principal.html', name=user['name'], picture="img/"+user['picture'])

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
        #message = services.text_Mensagem(number, text)
        
        print(number)
        print(text)

        #print("message = "+str(message))
        return 'OK'
    except Exception as e:
        return 'não enviado '+str(e)


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
        return 'não enviado ' + str(e)

if __name__ == '__main__':
    app.run()