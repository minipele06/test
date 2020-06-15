#robo_advisor.py

from dotenv import load_dotenv
import os
import requests
import json
import csv
import pandas as pd

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

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

for x in reversed(ticker_list):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={x}&apikey={API_KEY}&datatype=csv"
    response = requests.get(url)        
    #VALIDATE REQUEST FOR STOCK TICKER
    if "Error" in response.text:
        print(f"{x} Is An Invalid Stock Symbol")
        ticker_list.remove(x)
    else:
        with open(f"data/{x}.csv", 'w') as f:
            writer = csv.writer(f)
            for line in response.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))

#credit: https://stackoverflow.com/questions/45978295/saving-a-downloaded-csv-file-using-python

for x in ticker_list:
    print("-------------------------")
    print(f"YOUR SELECTED SYMBOL: {x}")
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