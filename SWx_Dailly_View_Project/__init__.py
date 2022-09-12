import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import app_config

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(env_name):
    """
    Create app
    """

    # Initialize the main application.
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    app.logger.info("Environment variable configured with app")

    # initialize other libraries
    app.logger.info("Started Initializing libraries with app")

    db.init_app(app)
    migrate.init_app(app=app, db=db)
    bcrypt.init_app(app)
    marshmallow.init_app(app)
    jwt.init_app(app)
    app.logger.info("Complete Initializing libraries with app")

    with app.app_context():
        # import routes
        from SWx_Dailly_View_Project.kp_forecast import routes as kp_forecast
        # register blueprint
        app.register_blueprint(kp_forecast.kp_blueprint)
        app.logger.info("Registered Blueprints with app")

        # common error handler
        # create tables if it not already exists
        # db.create_all()
        return app
