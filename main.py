# test
from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='aaa')

@app.route('/criar', methods=['POST',])
def criar():
    numero = request.form['numero']
    return render_template('lista.html', novo = numero)



app.run(debug=True)
