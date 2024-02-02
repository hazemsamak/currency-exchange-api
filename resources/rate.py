
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from components.auth.decorators import require_app_key
from exchange_rate.client import ExchangeRateClient
from schemas import DefaultsRateSchema, RateConverterSchema

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
        
        USD_EGP = round(client.exchange_converter(from_currency= 'USD', to_currency= 'EGP', black_market=False),2)
        AED_EGP = round(client.exchange_converter(from_currency= 'AED', to_currency= 'EGP', black_market=False),2)
        rates = {"USD": USD_EGP, "AED": AED_EGP}

        USD_EGP_bm = round(client.exchange_converter(from_currency= 'USD', to_currency= 'EGP', black_market=True),2)
        AED_EGP_bm = round(client.exchange_converter(from_currency= 'AED', to_currency= 'EGP', black_market=True),2)
        rates_bm = {"USD": USD_EGP_bm, "AED": AED_EGP_bm}
        return {"rates": rates, "rates_bm": rates_bm}

@blp.route("/converter")
class RateConverter(MethodView):
    @blp.arguments(RateConverterSchema, location="query")
    @blp.response(200, RateConverterSchema())
    @require_app_key
    def get(cls, args):
        from_currency_symbol = args["from_currency"]
        to_currency_symbol = args["to_currency"]
        black_market_flag = args["black_market"]
        try:
            rate = client.exchange_converter(from_currency= from_currency_symbol, to_currency= to_currency_symbol, black_market=black_market_flag)
            convertion = {**args, "rate":rate}
        except:
            abort(400, "Error message")
        return convertion
