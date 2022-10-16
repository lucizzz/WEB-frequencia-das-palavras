from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='lista')

@app.route('/criar', methods=['POST',])
def criar():
    numero = request.form['numero']
    numero2 = request.form['numero2']
    if numero.isnumeric() and numero2.isnumeric(): #isnumeric() função do python para verificar se é um numero
        numero = int(numero)
        numero2 = int(numero2)
        resul = numero+numero2
        return render_template('lista.html', titulo='lista', aa=resul)
    else:
        return render_template('lista.html', titulo='lista', aa="Não é int")






app.run(debug=True)
