import os

import sentry_sdk
from dotenv import load_dotenv
from flask import Flask
from flask_caching import Cache


from config import app_config

load_dotenv()
cache = Cache()

DNS_FOR_SENTRY = os.getenv("DNS_FOR_SENTRY")


def create_app(env_name):
    """
    Creates main FLASK app with all necessary initialization
    [   Here we included --> sentry integration [ for errors monitoring ],
        Registering Flask API BLUEPRINTS from respective Folder's routes  ]
    """

    # sentry initialization
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_sdk.init(
        dsn=DNS_FOR_SENTRY,
        integrations=[
            FlaskIntegration(),
        ],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0
    )

    # Initialize the main application.
    app = Flask(__name__)
    app.config['CACHE_TYPE'] = os.getenv('CATCH_TYPE')

    cache.init_app(app)

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
