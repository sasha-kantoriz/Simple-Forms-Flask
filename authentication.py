from flask_login import LoginManager, UserMixin


login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(_id):
    return User(_id)

class User(UserMixin):
    def __init__(self, _id):
        self.id = _id