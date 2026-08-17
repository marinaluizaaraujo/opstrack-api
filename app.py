from flask import Flask

app = Flask (__name__)

# Teste de diff :)
@app.route('/')
def status():
    return {'Servico': 'OpsTrackAPI', 'status': 'online'}

if __name__ == '__main__':
    app.run(debug=True)