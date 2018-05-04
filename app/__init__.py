from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config


bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.index'


def create_app(config_name):
    """
    Application Factory funtion. Passes a config object and instantiates
    components needed for application.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login.init_app(app)

    """
    Register Blueprint section
    """
    # Register Main blueprint/module
    from .main import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    # Register Authentication blueprint/module
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Register Error Handling blueprint/module
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    # Register SQLite blueprint/module
    from app.sql import bp as sql_bp
    app.register_blueprint(sql_bp)

    return app
