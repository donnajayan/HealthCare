

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import FlaskForm,CSRFProtect




app = Flask(__name__)

app.config['UPLOAD_FOLDER']="private/static/uploads"
app.config['SECRET_KEY'] = '8ea2a86e42689205dde0ba81f31138b6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///private.db'



db = SQLAlchemy(app)

login_manager = LoginManager(app) 



from private import routes