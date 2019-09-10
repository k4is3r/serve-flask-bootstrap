#importing the form in flask
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
#importing a data validator from WTF
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')