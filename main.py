from flask import Flask, request, redirect , make_response, render_template
#importin bootstrap
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


todos = ['Hacer cafe','Comprar Macbook','Mandar correos','Arreglar presupuesto','Comprar accesorios']

@app.route('/')
def index():
    user_ip= request.remote_addr 
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip,
        'todos' : todos,
    }
    
    return render_template('hello.html', **context)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)
