
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import DefaultsRateSchema, RateConverterSchema
from exchange_rate.client import ExchangeRateClient
from components.auth.decorators import require_app_key



blp = Blueprint("Rates", "rates", url_prefix='/sharks/currency-exchange', description="Operations on rates")
client = ExchangeRateClient()


def get_exchange_rates():
    exchange_rates = client.get_cached_rates()
    return exchange_rates

@blp.route("/defaults")

class RateList(MethodView):
    @blp.response(200, DefaultsRateSchema())
    @require_app_key
    def get(cls):
        
        USD_EGP = round(client.exchange_converter(from_currency= 'USD', to_currency= 'EGP'),2)
        AED_EGP = round(client.exchange_converter(from_currency= 'AED', to_currency= 'EGP'),2)
        rates = {"USD": USD_EGP, "AED": AED_EGP}
        return {"rates": rates}

@blp.route("/converter")
class RateConverter(MethodView):
    @blp.arguments(RateConverterSchema, location="query")
    @blp.response(200, RateConverterSchema())
    @require_app_key
    def get(cls, args):
        from_currency_symbol = args["from_currency"]
        to_currency_symbol = args["to_currency"]
        try:
            rate = client.exchange_converter(from_currency= from_currency_symbol, to_currency= to_currency_symbol)
            convertion = {**args, "rate":rate}
        except:
            abort(400, "Error message")
        return convertion
