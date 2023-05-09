from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.secret_key = 'some secret salt'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/coursework'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db=SQLAlchemy(app)
login_manager=LoginManager(app)
from web_app.models import User
from web_app.views import views
from web_app.views import auth, tests_func, test_func,courses_func






