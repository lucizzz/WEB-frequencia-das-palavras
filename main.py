# test
from flask import Flask
from flask import Flask, render_template, request

def frequencia(texto, palavra):
    lista_texto = texto.split()
    # lista_palavra = palavra.split()
    cont = 0
    for i in lista_texto:
        if palavra == i:
            cont+=1
    return cont

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        texto = request.form['texto']
        palavra = request.form['palavra']
        res = frequencia(texto, palavra)
        return render_template('lista.html', novo = res)
    else:
        return render_template('lista.html')
        
app.run(debug=True)
