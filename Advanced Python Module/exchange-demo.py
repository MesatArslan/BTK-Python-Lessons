import requests
import json

api_url = "https ://api.exchangeratesapi.io/latest?base="

currency_exchange =input("Type of Currency Exchange: ")
currency_received =input("Type of Currency Received: ")
amount = int(input(f"How many {currency_exchange} do you want to exchange?: "))

result= requests.get(api_url+currency_exchange)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(currency_exchange,result["rates"][currency_received], currency_received))

print("{0} {1} = {2} {3}".format(amount, currency_exchange, amount*result["rates"][currency_received], currency_received))