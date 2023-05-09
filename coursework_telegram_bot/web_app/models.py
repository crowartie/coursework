from flask_login import UserMixin
from web_app import db, login_manager


class User(db.Model, UserMixin):
    __tablename__ = 'app_account'
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    username = db.Column(db.String(128))
    login = db.Column(db.String(64))
    password = db.Column(db.String(120))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
