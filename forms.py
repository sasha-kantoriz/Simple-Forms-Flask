from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.fields.html5 import EmailField, TelField # can be accessed under the wtforms.fields.html5 namespace

class UserForm(FlaskForm):
    name = StringField('Name:', id='name')
    phone = TelField('Phone Number:', id='phone')
    email = EmailField('Email:', id='email')
    job = StringField('Job Title:', id='job')


class ChildForm(UserForm):
    parent_id = IntegerField()


class LoginForm(FlaskForm):
    password = PasswordField('Password', id='password')