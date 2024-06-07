from flask import Flask, render_template, request, redirect

app = Flask(__name__)

login = []
agendas = []
num = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/agendamento')
def agendamento():
    return render_template('agendamento.html')

@app.route('/pagina-inicial')
def pagina_inicial():
    return render_template('pagina-inicial.html', agendas=agendas, login=login)

@app.route('/calculo-idade')
def calculo_idade():
    return render_template('calc_idade.html')

@app.route('/calc-soro-medicamento')
def calc_soro_medicamento():
    return render_template('calc-medicamento-soro.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        codigo = len(login)
        nome_animal = request.form['nome-animal']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nome_tutor = request.form['nome-tutor']
        telefone = request.form['telefone']
        login.append((codigo, nome_tutor, telefone, nome_animal, especie, raca, peso))
        return redirect('/pagina-inicial')
    return render_template('cadastro.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    codigo = len(agendas)
    nome_do_animal = request.form['nome_do_animal']
    nome_do_tutor = request.form['nome_do_tutor']
    data = request.form['data']
    hora = request.form['hora']
    sintomas = request.form['sintomas']
    agendas.append((codigo, nome_do_animal, nome_do_tutor, data, hora, sintomas))
    return redirect('/pagina-inicial')

@app.route('/editar_agendamento/<int:codigo>', methods=['GET', 'POST'])
def editar_consulta(codigo):
    if request.method == 'POST':
        nome_do_animal = request.form['nome_do_animal']
        nome_do_tutor = request.form['nome_do_tutor']
        data = request.form['data']
        hora = request.form['hora']
        sintomas = request.form['sintomas']
        agendas[codigo] = (codigo, nome_do_animal, nome_do_tutor, data, hora, sintomas)
        return redirect('/pagina-inicial')
    else:
        agenda = agendas[codigo]
        return render_template('agendamento.html', agenda=agenda)

@app.route('/editar_login/<int:codigo>', methods=['GET', 'POST'])
def editar_login(codigo):
    if request.method == 'POST':
        nome_animal = request.form['nome-animal']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nome_tutor = request.form['nome-tutor']
        telefone = request.form['telefone']
        login[codigo] = (codigo, nome_tutor, telefone, nome_animal, especie, raca, peso)
        return redirect('/pagina-inicial')
    else:
        logins = login[codigo]
        return render_template('cadastro.html', login=logins)

@app.route('/cancelar_agendamento/<int:codigo>')
def cancelar_consulta(codigo):
    del agendas[codigo]
    return redirect('/pagina-inicial')

@app.route('/calulando-idade', methods=['GET','POST'])
def calculando_idade():
    result = ''
    if request.method == 'POST':
        animal = request.form['animal'].lower()
        idade = int(request.form['idade'])
        if animal == 'cachorro':
            if idade == 1:
                result = 'Seu Cachorro tem 15 anos humanos.'
            elif idade == 2:
                result = 'Seu Cachorro tem 24 anos humanos.'
            elif idade == 3:
                result = 'Seu Cachorro tem 28 anos humanos.'
            elif idade == 4:
                result = 'Seu Cachorro tem 32 anos humanos.'
            elif idade == 5:
                result = 'Seu Cachorro tem 36 anos humanos.'
            elif idade == 6:
                result = 'Seu Cachorro tem 40 anos humanos.'
            elif idade == 7:
                result = 'Seu Cachorro tem 44 anos humanos.'
            elif idade >= 8:
                idade_cachorro = 44 + (5 * (idade - 8))
                result = f'Seu Cachorro tem {idade_cachorro} anos humanos.'
        elif animal == 'gato':
            if idade == 1:
                result = 'Seu Gato tem 15 anos humanos.'
            elif idade == 2:
                result = 'Seu Gato tem 24 anos humanos.'
            elif idade == 3:
                result = 'Seu Gato tem 28 anos humanos.'
            elif idade == 4:
                result = 'Seu Gato tem 32 anos humanos.'
            elif idade == 5:
                result = 'Seu Gato tem 36 anos humanos.'
            elif idade >= 6:
                idade_gato = 36 + (4 * (idade - 6))
                result = (f'Seu Gato tem {idade_gato} anos humanos.')
        else:
            result = 'Animal Inválido'
    return render_template('calc_idade.html', result=result)

@app.route('/fluidoterapia', methods=['POST'])
def fluidoterapia():
    peso = int(request.form['peso_fluidoterapia'])
    if request.form['desidratacao'] == 'leve':
        volume = 50 * peso
    elif request.form['desidratacao'] == 'moderada':
        volume = 75 * peso
    elif request.form['desidratacao'] == 'grave':
        volume = 100 * peso
    else:
        volume = 0
    return render_template('calc-medicamento-soro.html', volume=volume)

@app.route('/dose-medicamento', methods=['POST'])
def dose_medicamento():
    peso = int(request.form['peso_medicamento'])
    dose = int(request.form['dose_recomendada'])
    dose_r = peso * dose
    return render_template('calc-medicamento-soro.html', dose=dose_r)

if __name__ == '__main__':
    app.run(debug=True)