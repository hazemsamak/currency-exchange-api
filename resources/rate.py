from datetime import datetime as dt
from datetime import timedelta as td
from dateutil import parser
import json
import redis

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import RateSchema
from exchange_rate.client import ExchangeRateClient



blp = Blueprint("Rates", "rates", description="Operations on rates")

redis_host = "redis-server"
redis_port = 6379
redis_password = ""

@blp.route("/rate")
class RateList(MethodView):
    # @blp.response(200, RateSchema(many=True))
    def get(cls):
        format = '%b %d %Y %I:%M%p'  # The format
        current_time = dt.utcnow()
        one_hour_ago = current_time - td(hours=1)
        two_hours_ago = current_time - td(hours=2)
        
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        
        time_created_str = r.get("rates:time_created")
        if not time_created_str:
            time_created_str = two_hours_ago.strftime(format)
            r.set("rates:time_created",time_created_str)
            
        time_created = parser.parse(time_created_str)
        print(one_hour_ago)
        if  time_created > one_hour_ago:
            exchange_rates = json.loads(r.get("rates:exchange_rates"))
        else:
            client = ExchangeRateClient()
            exchange_rates = client.list_rates()

            current_time_str = current_time.strftime(format)
            r.set("rates:time_created",current_time_str)
            r.set("rates:exchange_rates", json.dumps(exchange_rates))

        return exchange_rates, 200
