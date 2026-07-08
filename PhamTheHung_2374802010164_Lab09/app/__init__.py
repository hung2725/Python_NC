from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # blueprint.auth route

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # config file

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # import blueprints
    from app.routes import main as main_bp
    from app.auth_routes import auth as auth_bp

    # register blueprints
    app.register_blueprint(main_bp)         # route /, /about
    app.register_blueprint(auth_bp, url_prefix='/auth')  # /auth/login, /auth/register

    return app
