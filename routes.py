from flask import render_template, request, redirect, abort, url_for
from flask_login import login_required
import forms


""" 
Generate the login form (using flask) for the index.html page, where you will 
enter a new user. The form itself is created in forms.py. 
The index() route method is called from app.py
"""

def index():
    from app import get_all_rows_from_table
    rows = get_all_rows_from_table()
    return render_template('index.html', users=rows)

""" 
Retrieve all the rows from the database and return them.
All the data will be displayed on entire_database.html file.
The view_database() route method is called from app.py
"""
@login_required
def view_database():
    from app import get_all_rows_from_table
    rows = get_all_rows_from_table()
    return render_template('table.html', rows=rows)

def obtain_user(_id):
    from app import get_user_by_id, update_user
    user = get_user_by_id(_id)
    if not user:
        return abort(404, 'Not Found')
    modify_user_form = forms.UserForm()
    if request.method == 'POST':
        update_user(_id, modify_user_form.name.data, modify_user_form.phone.data, modify_user_form.email.data)
    return render_template('modify_user.html', _id=_id, form=modify_user_form, user=user)
def obtain_chlidren(parent_id):
    from app import update_child, get_user_by_id
    parent = get_user_by_id(parent_id)
    if not parent:
        return abort(404, 'Not Found')
    return render_template('children.html', rows=parent['children'])


def obtain_child(_id):
    from app import update_child, get_child_by_id
    form = forms.ChildForm()
    child = get_child_by_id(_id)
    if not child:
        return abort(404, 'Not Found')
    if request.method == 'POST':
        update_child(_id, form.name.data, form.phone.data, form.email.data)
    return render_template('modify_child.html', _id=_id, form=form, child=child)
def modify_database(the_id ,modified_category):
    if request.method == 'POST':
        from app import modify_data
        # Get data from the form on database page
        user_input = request.form[modified_category]
        # modify the row from the database
        modify_data(the_id, modified_category, user_input)
        # redirect back to the database page
        return redirect(url_for('index'))
    return redirect(url_for('index'))

def delete_parent(_id):
    from app import delete_user
    # if the checkbox was selected (for deleting entire row)
    delete_user(_id)
    return redirect(url_for('index'))

def delete_child(_id):
    from app import delete_child
    # if the checkbox was selected (for deleting entire row)
    delete_child(_id)
    return redirect(url_for('index'))

def submitted():
    from app import insert_user_data, insert_child_data

    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']

    if request.form.get('child'):
        parent_id = request.form['parent_id']
        child = insert_child_data(name, phone, email, parent_id)
        return dict(child)

    # insert data into database
    user = insert_user_data(name, phone, email)
    return dict(user)
