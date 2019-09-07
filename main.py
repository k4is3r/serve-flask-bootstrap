from flask import Flask, request, redirect , make_response, render_template, session, url_for 
#importin bootstrap
from flask_bootstrap import Bootstrap
#importin whta the form in flask
from flask_wtf import FlaskForm 
from wtforms.fields import StringField, PasswordField, SubmitField
#importin a data validator from WTF
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)

#setting some configuration for implent flask session
app.config['SECRET_KEY'] = 'SUPER SECRETO'


todos = ['Hacer cafe','Comprar Macbook','Mandar correos','Arreglar presupuesto','Comprar accesorios']

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')


@app.route('/')
def index():
    user_ip= request.remote_addr 
    response = make_response(redirect('/hello'))
    #response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['GET','POST'])
def hello():
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip' : user_ip,
        'todos' : todos,
        'login_form' : login_form,
        'username' : username,
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        return redirect(url_for('index'))


    return render_template('hello.html', **context)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)
