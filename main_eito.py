from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_volume(desidratacao, peso):
    if desidratacao == 'leve':
        volume = 50 * peso
    elif desidratacao == 'moderada':
        volume = 75 * peso
    elif desidratacao == 'grave':
        volume = 100 * peso
    else:
        volume = 0
    return render_template('calc-medicamento-soro.html', volume=volume)

@app.route('/', methods=['GET', 'POST'])
def index():
    volume = None
    dose = None
    if request.method == 'POST':
        if 'peso_fluidoterapia' in request.form:
            grau_desidratacao = request.form['desidratacao']
            peso = float(round(request.form['peso_fluidoterapia']),2)
            volume = calcular_volume(grau_desidratacao, peso)
        if 'peso_medicamento' in request.form:
            peso = float(request.form['peso_medicamento'])
            dose_recomendada = float(request.form['dose_recomendada'])
            dose = peso * dose_recomendada
    return render_template('calc_medicamento_calc_soro.html', volume=volume, dose=dose)

if __name__ == '__main__':
    app.run(debug=True)
