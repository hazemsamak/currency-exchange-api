import requests
import json
import os

class ExchangeRateClient():
    def list_rates(self):
        print("Call Exchange Rates API")
        api_key = os.getenv("CURRENCY_EXCHANGE_RATES_API_KEY","")
        url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}&symbols=AED,EGP"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)
        # with open("rates_file.json", 'r', encoding='utf-8') as f:
        #     response = json.load(f)
        rates = response["rates"]
        USD = rates["EGP"]
        AED = round(rates["EGP"] / rates["AED"],2)
        results = {"USD": USD, "AED": AED}
        return results

# exchangeRateClient = ExchangeRateClient()
# print(exchangeRateClient.list_rates())