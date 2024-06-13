from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Listas para armazenar dados de login e agendas
login = []
agendas = []
num = 0

@app.route('/')
def index():
    # Renderiza a página de índice
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    # Renderiza a página de cadastro
    return render_template('cadastro.html')

@app.route('/agendamento')
def agendamento():
    # Renderiza a página de agendamento
    return render_template('agendamento.html')

@app.route('/pagina-inicial')
def pagina_inicial():
    # Renderiza a página inicial com agendas e dados de login
    return render_template('pagina-inicial.html', agendas=agendas, login=login)

@app.route('/calculo-idade')
def calculo_idade():
    # Renderiza a página de cálculo de idade
    return render_template('calc_idade.html', login=login)

@app.route('/calc-soro-medicamento')
def calc_soro_medicamento():
    # Renderiza a página de cálculo de medicamento e soro
    return render_template('calc-medicamento-soro.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        # Lida com o envio do formulário de cadastro
        codigo = len(login)
        nome_animal = request.form['nome-animal']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nome_tutor = request.form['nome-tutor']
        telefone = request.form['telefone']
        login.append((codigo, nome_tutor, telefone, nome_animal, especie, raca, peso))
        return redirect('/pagina-inicial')
    # Renderiza a página de cadastro
    return render_template('cadastro.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    # Lida com o envio do formulário de agendamento
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
        # Lida com o envio do formulário para editar um item de agenda
        nome_do_animal = request.form['nome_do_animal']
        nome_do_tutor = request.form['nome_do_tutor']
        data = request.form['data']
        hora = request.form['hora']
        sintomas = request.form['sintomas']
        agendas[codigo] = (codigo, nome_do_animal, nome_do_tutor, data, hora, sintomas)
        return redirect('/pagina-inicial')
    else:
        # Renderiza a página de agendamento com o item de agenda específico
        agenda = agendas[codigo]
        return render_template('agendamento.html', agenda=agenda)

@app.route('/editar_login/<int:codigo>', methods=['GET', 'POST'])
def editar_login(codigo):
    if request.method == 'POST':
        # Lida com o envio do formulário para editar um item de login
        nome_animal = request.form['nome-animal']
        especie = request.form['especie']
        raca = request.form['raca']
        peso = request.form['peso']
        nome_tutor = request.form['nome-tutor']
        telefone = request.form['telefone']
        login[codigo] = (codigo, nome_tutor, telefone, nome_animal, especie, raca, peso)
        return redirect('/pagina-inicial')
    else:
        # Renderiza a página de cadastro com o item de login específico
        logins = login[codigo]
        return render_template('cadastro.html', login=logins)

@app.route('/cancelar_agendamento/<int:codigo>')
def cancelar_consulta(codigo):
    # Lida com o cancelamento de um item de agenda específico
    del agendas[codigo]
    return redirect('/pagina-inicial')

@app.route('/calculando-idade', methods=['GET','POST'])
def cal_idade():
    result = ''
    if request.method == 'POST':
        # Lida com o cálculo de idade com base na entrada do usuário
        animal = request.form['animal'].lower()
        idade = int(request.form['idade'])
        if animal == 'cachorro':
            if idade == 1:
                result = 'Seu Cachorro tem 15 anos humanos'
            elif idade == 2:
                result = 'Seu Cachorro tem 24 anos humanos'
            elif idade == 3:
                result = 'Seu Cachorro tem 28 anos humanos'
            elif idade == 4:
                result = 'Seu Cachorro tem 32 anos humanos'
            elif idade == 5:
                result = 'Seu Cachorro tem 36 anos humanos'
            elif idade == 6:
                result = 'Seu Cachorro tem 40 anos humanos'
            elif idade == 7:
                result = 'Seu Cachorro tem 44 anos humanos'
            elif idade >= 8:
                idade_cachorro = 44 + (5 * (idade - 8))
                result = f'Seu Cachorro tem {idade_cachorro} anos humanos'
        elif animal == 'gato':
            if idade == 1:
                result = 'Seu Gato tem 15 anos humanos'
            elif idade == 2:
                result = 'Seu Gato tem 24 anos humanos'
            elif idade == 3:
                result = 'Seu Gato tem 28 anos humanos'
            elif idade == 4:
                result = 'Seu Gato tem 32 anos humanos'
            elif idade == 5:
                result = 'Seu Gato tem 36 anos humanos'
            elif idade >= 6:
                idade_gato = 36 + (4 * (idade - 6))
                result = (f'Seu Gato tem {idade_gato} anos humanos')
        else:
            result = 'Animal Inválido'
    # Renderiza a página de cálculo de idade com o resultado
    return render_template('calc_idade.html', result=result)

@app.route('/fluidoterapia', methods=['POST'])
def fluidoterapia():
    # Lida com o cálculo de volume de fluidoterapia
    peso = int(request.form['peso_fluidoterapia'])
    if request.form['desidratacao'] == 'leve':
        volume = 50 * peso
    elif request.form['desidratacao'] == 'moderada':
        volume = 75 * peso
    elif request.form['desidratacao'] == 'grave':
        volume = 100 * peso
    else:
        volume = 0
    # Renderiza a página de cálculo de medicamento e soro com o volume
    return render_template('calc-medicamento-soro.html', volume=volume)

@app.route('/dose-medicamento', methods=['POST'])
def dose_medicamento():
    # Lida com o cálculo de dosagem de medicamento
    peso = int(request.form['peso_medicamento'])
    dose = int(request.form['dose_recomendada'])
    dose_r = peso * dose
    # Renderiza a página de cálculo de medicamento e soro com a dosagem
    return render_template('calc-medicamento-soro.html', dose=dose_r)

if __name__ == '__main__':
    # Executa a aplicação Flask em modo de depuração
    app.run(debug=True)