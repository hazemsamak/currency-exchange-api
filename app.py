import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_smorest import Api

from resources.disk_usage import blp as DeskUsageBlueprint
from resources.loopback import blp as LoopbackBlueprint
from resources.prayers import blp as PrayersBlueprint
from resources.rate import blp as RateBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()
    app.config["API_TITLE"] = "Sharks REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/sharks"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["PROPAGATE_EXCEPTIONS"] = True
    api = Api(app)
    api.register_blueprint(RateBlueprint)
    api.register_blueprint(LoopbackBlueprint)
    api.register_blueprint(PrayersBlueprint)
    api.register_blueprint(DeskUsageBlueprint)
    return app
