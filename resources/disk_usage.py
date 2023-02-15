
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from components.auth.decorators import require_app_key
from disk_usage.client import DiskUsageClient
from schemas import DeskUsageSchema

blp = Blueprint("Disk Usage", "disk_usage", url_prefix='/sharks/desk-usage', description="Desk Utilization")
client = DiskUsageClient()


@blp.route("/utilization")
class RateList(MethodView):
    @blp.response(200, DeskUsageSchema())
    @require_app_key
    def get(cls):
        
        try:
            utilization = client.get_disk_space()
        except:
            abort(400, "Can't get the Desk Utilization")
        return {"utilization": utilization}

