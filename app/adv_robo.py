#robo_advisor.py

from dotenv import load_dotenv
import os
import requests
import json
import pandas as pd

load_dotenv()

print(os.getenv("ALPHAVANTAGE_API_KEY"))

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo&datatype=csv"
response = requests.get(request_url)
# response_data = json.loads(response.text)
# print(response_data["Time Series (5min)"]["2020-06-12 16:00:00"])

print(response.text)

df = pd.read_csv(request_url)   

df.to_csv("data/IBM.csv")

ticker_list = []

while True:
    try:
        symbol = input("Please Enter Your Stock Symbol: ")
        if symbol.isalpha() == False:
            print("Invalid Stock Symbol, Try Again")
        elif len(symbol) > 4:
            print("Invalid Stock Symbol, Try Again")
        elif symbol.capitalize() == "Done":
            break
        else:
            ticker_list.append(symbol.upper())
    except ValueError:
        print("Invalid Stock Symbol, Try Again")

print("-------------------------")
print(f"YOUR SELECTED SYMBOL: {ticker_list}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")