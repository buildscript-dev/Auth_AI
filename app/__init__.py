from flask import Flask
from .extensions import db, login_manager, bcrypt
from .auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return "Welcome to the Login Web!"

    return app
