from flask import Flask

from config import app_config


def create_app(env_name):
    """
    Create app
    """

    # Initialize the main application.
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    app.logger.info("Environment variable configured with app")

    with app.app_context():

        # import routes
        from SWx_Dailly_View_Project.kp_forecast import routes as kp_forecast
        from SWx_Dailly_View_Project.goes_proton_flux import routes as proton_flux
        from SWx_Dailly_View_Project.latitude_index import routes as latitude_index

        # register blueprint
        app.register_blueprint(kp_forecast.kp_blueprint)
        app.register_blueprint(proton_flux.proton_flux_blueprint)
        app.register_blueprint(latitude_index.latitude_blueprint)
        app.logger.info("Registered Blueprints with app")

        return app
