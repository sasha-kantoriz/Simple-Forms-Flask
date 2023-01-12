# from flask_login import load_user
#
#
# @load_user
# def user_loader()
from flask import Blueprint, redirect, request, render_template
from flask_login import login_user, logout_user

import forms
import authentication

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        if form.password.data == 'App Secret':
            user = authentication.User(1)
            login_user(user)
            return redirect(request.args.get('next', '/'))
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/')
