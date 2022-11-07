import requests
import json
import os
import redis
from datetime import datetime as dt
from datetime import timedelta as td
from dateutil import parser

redis_host = os.getenv("REDIS_DB_URI","localhost")
redis_port = 6379
redis_password = ""

class ExchangeRateClient():
    

    def list_rates(self):
        print("Call Exchange Rates API")
        api_key = os.getenv("CURRENCY_EXCHANGE_RATES_API_KEY","")
        url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)
        rates = response["rates"]
        # USD = rates["EGP"]
        # AED = round(rates["EGP"] / rates["AED"],2)
        # results = {"USD": USD, "AED": AED}
        return rates
    
    def get_cached_rates(self):
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
            exchange_rates = self.list_rates()

            current_time_str = current_time.strftime(format)
            r.set("rates:time_created",current_time_str)
            r.set("rates:exchange_rates", json.dumps(exchange_rates))
        
        return exchange_rates
    
    def exchange_converter(self, from_currency :str, to_currency :str):
        exchange_rates = self.get_cached_rates()

        from_currency_rate = 1 if from_currency == "USD" else exchange_rates[from_currency]
        to_currency_rate = 1 if to_currency == "USD" else exchange_rates[to_currency]

        rate = round(1 * to_currency_rate / from_currency_rate,4)

        return rate

# exchangeRateClient = ExchangeRateClient()
# print(exchangeRateClient.list_rates())