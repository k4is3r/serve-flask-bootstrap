from flask import request, redirect , make_response, render_template, session, url_for, flash 
#importing bootstrap
from flask_bootstrap import Bootstrap
#importing for use in the testing section
import unittest
from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users

app = create_app()

todos = ['Hacer cafe','Comprar Macbook','Mandar correos','Arreglar presupuesto','Comprar accesorios']


#defining the test section
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.route('/')
def index():
    user_ip= request.remote_addr 
    response = make_response(redirect('/hello'))
    #response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['GET'])
def hello():
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    username = session.get('username')
    context = {
        'user_ip' : user_ip,
        'todos' : todos,
        'username' : username,
    }

    
    return render_template('hello.html', **context)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)
