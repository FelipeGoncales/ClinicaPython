from flask import Flask, render_template, request, redirect

app = Flask(__name__)

agendas = []


@app.route('/')
def index():
    return render_template('index.html', agendas=agendas)

@app.route('/agendamento', methods=['GET', 'POST'])
def agendamento():
    if request.method == 'POST':
        codigo = len(agendas)
        nome_do_animal = request.form['nome_do_animal']
        nome_do_tutor = request.form['nome_do_tutor']
        data = request.form['data']
        hora = request.form['hora']
        sintomas = request.form['sintomas']
        agendas.append((codigo, nome_do_animal, nome_do_tutor, data, hora, sintomas))
        return redirect('/')
    return render_template('agendamento.html')

@app.route('/editar_agendamento/<int:codigo>', methods=['GET', 'POST'])
def editar_consulta(codigo):
    if request.method == 'POST':
        data = request.form['data']
        hora = request.form['hora']
        sintomas = request.form['sintomas']
        agendas[codigo] = (codigo, agendas[codigo][1], agendas[codigo][2], data, hora, sintomas)
        return redirect('/')
    else:
        agenda = agendas[codigo]
        return render_template('agendamento.html', agenda=agenda)

@app.route('/cancelar_agendamento/<int:codigo>')
def cancelar_consulta(codigo):
    del agendas[codigo]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)