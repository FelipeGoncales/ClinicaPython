from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
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

if __name__ == '__main__':
    app.run(debug=True)