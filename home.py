from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
    nome = request.form['nome']
    cognome = request.form['cognome']
    data_nascita = request.form['data_nascita']
    nazione = request.form['nazione']
    username = request.form['username']
    password = request.form['password']
    confermapassword = request.form['confermapassword']
    lingue = request.form.getlist('lingue')
    Acconsenso = request.form['Acconsenso']
    email = request.form['email']
    if password != confermapassword:
        return('Password diverse')
    elif nome == "" or cognome == '' or username == '' or password == '' or confermapassword == '' or email == '':
        return('Dati mancanti')
    else:
        return render_template('risultato.html', nome = nome, cognome = cognome,  data_nascita = data_nascita, nazione = nazione, username = username, password = password, confermapassword = confermapassword, Acconsenso= Acconsenso, email= email, lingue=lingue)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)