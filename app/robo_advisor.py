#robo_advisor.py

from dotenv import load_dotenv
import os
import requests
import csv
import pandas as pd
import datetime

load_dotenv()

def to_usd(my_price):
    return f"${my_price:,.2f}"

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

time = datetime.datetime.now()
today = time.strftime("%Y-%m-%d %I:%M %p")

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

stock_number = len(ticker_list)
count = 0

for x in ticker_list:
    count += 1
    csv_filepath = os.path.join((os.path.dirname(__file__)),"..", "data", f"{x}.csv")

    prices_df = pd.read_csv(csv_filepath)
    hundred_dma = to_usd(prices_df["close"].mean())
    fifty_dma = to_usd(prices_df["close"].head(50).mean())
    prices_dict = prices_df.to_dict("records")
    day = prices_dict[0]["timestamp"]
    close = to_usd(prices_dict[0]["close"])
    high = to_usd(prices_dict[0]["high"])
    low = to_usd(prices_dict[0]["low"])

    print("-------------------------")
    print(f"YOUR SELECTED SYMBOL: {x}")
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")
    print(f"REQUEST AT: {today}")
    print("-------------------------")
    print(f"LATEST DAY: {day}")
    print(f"LATEST CLOSE: {close}")
    print(f"RECENT HIGH: {high}")
    print(f"RECENT LOW: {low}")
    print("-------------------------")

    if close > hundred_dma and close > fifty_dma:
        print("RECOMMENDATION: STRONG BUY!")
        print("RECOMMENDATION REASON: Stock price is above the 50-DMA & 100-DMA")
    elif close > fifty_dma:
        print("RECOMMENDATION: BUY!")
        print("RECOMMENDATION REASON: Stock price is above the 50-DMA")
    elif close < hundred_dma and close < fifty_dma:
        print("RECOMMENDATION: STRONG SELL!")
        print("RECOMMENDATION REASON: Stock price is below the 50-DMA & 100-DMA")
    elif close < fifty_dma:
        print("RECOMMENDATION: SELL!")
        print("RECOMMENDATION REASON: Stock price is below the 50-DMA")

    if count == stock_number:
        print("-------------------------")
        print("HAPPY INVESTING!")
        print("-------------------------")