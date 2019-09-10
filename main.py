from flask import request, redirect , make_response, render_template, session, url_for, flash 
#importing bootstrap
from flask_bootstrap import Bootstrap
#importing for use in the testing section
import unittest
from app import create_app
from app.forms import TodoForm
from app.firestore_service import get_users, get_todos, put_todos
from flask_login import login_required, current_user

app = create_app()


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


@app.route('/hello', methods=['GET','POST'])
@login_required
def hello():
    #user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    context = {
        'user_ip' : user_ip,
        'todos' : get_todos(user_id=username) ,
        'username' : username,
        'todo_form': todo_form,
    }

    if todo_form.validate_on_submit():
        put_todos(user_id=username, description=todo_form.description.data)
        flash('Task created')
        return redirect(url_for('hello'))


    return render_template('hello.html', **context)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)
