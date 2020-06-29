# Robo-Advisor Project

## Functionality

This program allows you to enter multiple stocks and receive the following information based upon daily data:

* Last Day Traded
* The Latest Closing Price
* The Recent High (Last 100 Trading Days)
* The Recent Low (Last 100 Trading Days)
* Buy/Sell Recommendation Based Upon 50 & 100 Day Moving Averages

## Setup

### Repo Setup
Use [GitHub](https://github.com/minipele06/robo-advisor) to clone the project repository called "Robo-Advisor". Use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

>cd ~/Desktop/robo-advisor

### Environment Setup
Create and activate a new Anaconda virtual environment:

>conda create -n stocks-env python=3.7 # (first time only)

>conda activate stocks-env

From within the virtual environment, install the required packages specified in the "requirements.txt" file:

>pip install -r requirements.txt

### AlphaVantage Setup
The program will need an API Key to issue requests to the [AlphaVantage API](https://www.alphavantage.co/). Follow the link and signup for an account which will then issue you your individual API Key. You will then need to create a .env file to save your environment variable which should be labeled ALPHAVANTAGE_API_KEY.

>ALPHAVANTAGE_API_KEY="abc123"

## Instructions
From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

>python app/robo_advisor.py

If you receive a message to enter your stock symbol, then you have properly set up the program and may proceed.

## Step-by-Step Guide

As stated above, once you receive a message to enter your stock symbol, you are ready to use the program. 

You may enter as many stock tickers as you'd like (depending on the API Key, the free version allows you to pull 5 stocks per minute or 500 per day). Once you've completed entering in your desired symbols, type 'Done' the next time the program prompts you to enter a symbol. Your symbols will be validated to exclude alphanumeric inputs and inputs greater than 4 characters.

Once you have entered 'Done', the program will proceed to pull the corresponding data. If any symbols do not exist, the program will notify you.

Finally, the program will notify you of the information outlined in the functionality section.
