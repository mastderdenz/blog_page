from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
D_B = "database"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "spencer1010"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{D_B}'
    db.init_app(app)


    from .ui import ui
    from .login import authentication

    app.register_blueprint(ui, url_prefix="/")
    app.register_blueprint(authentication, url_prefix="/")

    from .models import User, Post, Comment, Like

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "authentication.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("website/" + D_B):
        with app.app_context():
            db.create_all()
            print("Database created!")



#packages for the app