from flask import Flask

app = Flask (__name__)

# Teste de diff :)
@app.route('/')
def status():
    return {'Servico': 'OpsTrackAPI', 'status': 'online'}

@app.route('/tickets')
def tickets():
    return {
        'tickets': [
            {'id': 1, 'titulo': 'Erro ao logar no sistema', 'status': 'aberto'},
            {'id': 2, 'titulo': 'Lentidão no relatório mensal', 'status': 'em andamento'},
            {'id': 3, 'titulo': 'Solicitação de novo acesso', 'status': 'fechado'}
        ]
    }

if __name__ == '__main__':
    app.run(debug=True)

