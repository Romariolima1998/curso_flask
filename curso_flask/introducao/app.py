from flask import Flask, Response, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# com decorator
# request
@app.route('/')
def index():
    titulo =request.args.get('titulo')
    data = dict(
        path=request.path,
        referrer=request.referrer,
        content_type = request.content_type,
        method=request.method,
        titulo=titulo
    )
    return data

# com funcao
def test():
    return '<h1> rota por funcao </h1>'

app.add_url_rule('/test', 'test', test)



# response
# nao e necessario usar o9response o flask ja faz por si so
@app.route("/response") # type: ignore
def response():
    headers = {
        'content_type': 'text/html'
    }
    return Response('uma resposta do servidor', 200, headers= headers)

# url dinamica com parametro de view

@app.route('/teste2')
@app.route('/teste2/<string:parametro>')
def teste2(parametro = 'vazio'):
    return f'url dinamica, parametro = {parametro}'

# redirect
@app.route('/redirect')
def redirect_():
    return redirect('/')

# redirect da forma certa
# redirect com url_for 'passe o nome da view em uma string
@app.route('/redirect2')
def redirect2():
    return redirect(url_for('index'))

# renderizando templates
@app.route('/template')
def template_():
    return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)