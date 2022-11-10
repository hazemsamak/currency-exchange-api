
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import LoopbackSchema

from components.auth.decorators import require_app_key



blp = Blueprint("Loopback", "loopback", url_prefix='/sharks', description="Loopback operation")

@blp.route("/loopback")
class Loopback(MethodView):
    @blp.response(200, LoopbackSchema())
    @require_app_key
    def get(cls):
        return {"message": "I'm alive"}
