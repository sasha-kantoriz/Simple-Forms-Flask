import os
from flask import Flask

from models import db
import authentication
import routes
import views


def create_the_database(database):
    if not os.path.exists(DB_DIR):
        os.mkdir(DB_DIR)
    database.create_all()


BASE_DIR = os.path.dirname(__file__)
DB_DIR = os.getenv('DB_DIR', os.path.join(BASE_DIR, 'database'))
DB_NAME = os.path.join(DB_DIR, 'info.db')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'App Secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # no warning messages
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_DIR}/info.db'  # for using the sqlite database
db.init_app(app)
authentication.login_manager.init_app(app)


all_methods = ['GET', 'POST']

# Home page (where you will add a new user)
app.add_url_rule('/', view_func=routes.index)

app.add_url_rule('/members', methods=all_methods, view_func=routes.all_members)
app.add_url_rule('/member/<string:_id>', methods=all_methods, view_func=routes.member_by_id)
app.add_url_rule('/delete/member/<string:_id>', view_func=routes.delete_member)
app.add_url_rule('/children/<string:_id>', view_func=routes.get_children)
app.add_url_rule('/parents/<string:_id>', view_func=routes.get_parents)
app.add_url_rule('/grandchildren/<string:_id>', view_func=routes.get_grandchildren)
app.add_url_rule('/grandparents/<string:_id>', view_func=routes.get_grandparents)
app.add_url_rule('/grandgrandchildren/<string:_id>', view_func=routes.get_grandgrand_children)
app.add_url_rule('/grandgrandparents/<string:_id>', view_func=routes.get_grandgrand_parents)

app.register_blueprint(views.auth)


# if database does not exist in the current directory, create it!
db_is_new = not os.path.exists(DB_NAME)
if db_is_new:
    with app.app_context():
        create_the_database(db)


# start the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
