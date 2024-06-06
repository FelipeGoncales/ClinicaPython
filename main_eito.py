from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_volume(desidratacao, peso):
    if desidratacao == 'leve':
        return 50 * peso
    elif desidratacao == 'moderada':
        return 75 * peso
    elif desidratacao == 'grave':
        return 100 * peso
    else:
        return 0

@app.route('/', methods=['GET', 'POST'])
def index():
    volume = None
    dose = None
    if request.method == 'POST':
        if 'peso_fluidoterapia' in request.form:
            grau_desidratacao = request.form['desidratacao']
            peso = float(request.form['peso_fluidoterapia'])
            volume = calcular_volume(grau_desidratacao, peso)
        if 'peso_medicamento' in request.form:
            peso = float(request.form['peso_medicamento'])
            dose_recomendada = float(request.form['dose_recomendada'])
            dose = peso * dose_recomendada
    return render_template('calc_medicamento_calc_soro.html', volume=volume, dose=dose)

if __name__ == '__main__':
    app.run(debug=True)
