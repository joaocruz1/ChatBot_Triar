from flask import Flask, request, redirect, render_template, url_for
import sett 
import services
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def  inicio():
    return 'Pagina inicial teste'


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login/auth', methods=['GET'])
def auth():
    f = open(url_for('static', 'users.json'))
    users = json.load(f.read())

    try:
        user = request.form['user']
        password = request.form['senha']
    except:
        return 'Formulário não preenchido corretamente'

    for u in users:
        if u['name'] == user and u['password'] == password:
            return redirect(url_for('principal'))
    
    return redirect(url_for('index?Auth=NotAuthorized'))


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