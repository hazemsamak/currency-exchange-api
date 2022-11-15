
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import PrayerTimingsSchema
from prayer_times.client import PrayerTimesClient
from components.auth.decorators import require_app_key



blp = Blueprint("Prayers", "prayers", url_prefix='/sharks/prayers-timings', description="Operations on Prayers")
client = PrayerTimesClient()


@blp.route("/timings")
class RateList(MethodView):
    @blp.response(200, PrayerTimingsSchema())
    @require_app_key
    def get(cls):
        
        try:
            timings = client.get_cached_prayer_timings()
        except:
            abort(400, "Can't get the Prayer Timings")
        return {"timings": timings}

