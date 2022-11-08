import os
from flask import Flask, jsonify
from flask_smorest import Api

from dotenv import load_dotenv 


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
    return app
