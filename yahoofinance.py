import json
import requests
import pandas
import yfinance as yf
import utils
from datetime import date

# asks user for a stock/ticker symbol
try:
    stock = input("Enter stock: ")

    data = yf.Ticker(stock)

    # endpoint 1
    url = "https://query1.finance.yahoo.com/v7/finance/quote"
    user_agent_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    query_str = {"symbols": stock}
    response = requests.request("GET", url, headers=user_agent_headers, params=query_str)
    stock_json = response.json()

    # Name Ticker, Full Name of the Stock
    tickerName = stock_json['quoteResponse']['result'][0]['symbol']
    fullName = stock_json['quoteResponse']['result'][0]['longName']

    # endpoint 2
    url2 = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/"
    query_str = {"symbol": stock, "modules":"financialData"}
    response = requests.request("GET",url2, headers=user_agent_headers,params=query_str)
    stock_json = response.json()

    # Current Price, Target Mean Price, Cash on Hand, Profit Margins
    currentPrice = stock_json['quoteSummary']['result'][0]['financialData']['currentPrice']
    targetMeanPrice = stock_json['quoteSummary']['result'][0]['financialData']['targetMeanPrice']
    cashOnHand = stock_json['quoteSummary']['result'][0]['financialData']['totalCash']
    profitMargins = stock_json['quoteSummary']['result'][0]['financialData']['profitMargins']

    print("Ticker Name: ", tickerName, "\n",
          "Full Name of Stock: ", fullName, "\n",
          "Current Price: ", currentPrice, "\n",
          "Target Mean Price: ", targetMeanPrice, "\n",
          "Cash on Hand: ", cashOnHand, "\n",
          "Profit Margins: ", profitMargins)

    today = date.today()
    d = today.strftime("%d/%m/%Y")

    # data to be written
    stock_info = {
        "Date": d,
        "Ticker Name": tickerName,
        "Full Name of Stock": fullName,
        "Current Price": currentPrice,
        "Target Mean Price": targetMeanPrice,
        "Cash on Hand": cashOnHand,
        "Profit Margins": profitMargins
    }

    # Serializing json
    json_object = json.dumps(stock_info, indent=4)

    # writing to json file
    with open("stock_information.json", "w") as outfile:
        outfile.write(json_object)
    print("Stock information stored in stock_information.json")

except:
    print("Error: Invalid stock or the API is unable to return information.")
