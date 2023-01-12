import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import authentication
import routes
import views

def create_the_database(db):
    db.create_all()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'A secret'
authentication.login_manager.init_app(app)


all_methods = ['GET', 'POST']

# Home page (where you will add a new user)
app.add_url_rule('/', view_func=routes.index)
# "Thank you for submitting your form" page
app.add_url_rule('/submit', methods=['POST'], view_func=routes.submitted)
# Viewing all the content in the database page
app.add_url_rule('/database', view_func=routes.view_database)
app.add_url_rule('/user/<string:_id>', view_func=routes.obtain_user, methods=all_methods)
app.add_url_rule('/children/<string:parent_id>', view_func=routes.obtain_chlidren, methods=all_methods)
app.add_url_rule('/child/<string:_id>', view_func=routes.obtain_child, methods=all_methods)
app.add_url_rule('/delete/user/<_id>', methods=all_methods, view_func=routes.delete_parent)
app.add_url_rule('/delete/child/<_id>', methods=all_methods, view_func=routes.delete_child)

app.register_blueprint(views.auth)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # no warning messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db' # for using the sqlite database

db = SQLAlchemy(app)

# Create User Table
class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(50))
    children = db.relationship('Child')

    def __iter__(self):
        return iter([('id', self.id), ('name', self.name), ('phone', self.phone), ('email', self.email), ('children', [dict(child) for child in self.children])])

class Child(db.Model):
    __tablename__ = 'Children'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(50))
    parent_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    def __iter__(self):
        return iter([('id', self.id), ('name', self.name), ('phone', self.phone), ('email', self.email), ('parent_id', self.parent_id)])


def insert_user_data(name, phone, email):
    new_user = User(name=name, phone=phone, email=email)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def insert_child_data(name, phone, email, parent_id):
    new_child = Child(name=name, phone=phone, email=email, parent_id=parent_id)
    db.session.add(new_child)
    db.session.commit()
    return new_child


def modify_data(the_id, col_name, user_input):
    the_user = User.query.filter_by(id=the_id).first()
    if col_name == 'name':
        the_user.name = user_input
    elif col_name == 'phone':
        the_user.phone = user_input 
    elif col_name == 'email':
        the_user.email = user_input 

    
    db.session.commit() 
def update_user(_id, name=None, phone=None, email=None):
    user = User.query.filter_by(id=_id).first()
    if name:
        user.name = name
    if phone:
        user.phone = phone
    if email:
        user.email = email
    db.session.commit()

def update_child(_id, name=None, phone=None, email=None):
    child = Child.query.filter_by(id=_id).first()
    if name:
        child.name = name
    if phone:
        child.phone = phone
    if email:
        child.email = email
    db.session.commit()

def delete_user(the_id):
    the_user = User.query.filter_by(id=the_id).first()
    db.session.delete(the_user)
    db.session.commit()
    
def delete_child(the_id):
    the_user = Child.query.filter_by(id=the_id).first()
    db.session.delete(the_user)
    db.session.commit()


def get_user_by_id(_id):
    the_user = User.query.filter_by(id=_id).first()
    if the_user:
        return dict(the_user)

def get_child_by_id(_id):
    child = Child.query.filter_by(id=_id).first()
    if child:
        return dict(child)

def get_all_rows_from_table():
    users = User.query.all()
    return [dict(user) for user in users]
    

# if database does not exist in the current directory, create it!
db_is_new = not os.path.exists('info.db')
if db_is_new:
    create_the_database(db)


# start the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
