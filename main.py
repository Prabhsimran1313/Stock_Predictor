from http import client
import requests
from twilio.rest import Client

account_sid ="AC6f6eed225fbd2d27b0d3987821480599"
auth_token ="b199da99ea0aa4c704e1f5c1e3a4e835"



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_key1 = "CXQJORX0XSWENMDW"
API_key2 = "71331e0ae233433fa3403a8d00c3590d"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey":API_key1
}

news_params = {"q": COMPANY_NAME,
                "apikey": API_key2
}
r = requests.get(STOCK_ENDPOINT, stock_params)
data = r.json()


data = r.json()["Time Series (Daily)"]
x = [ value for (key, value) in data.items()]
yesterday_data = x[0]
yesterday_closing_price = float(yesterday_data['4. close'])


day_before_yesterday_data = x[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data['4. close'])


difference_in_value = float(day_before_yesterday_closing_price-yesterday_closing_price)
up_down = None
if difference_in_value>0:
    up_down="🔼"
else:
    up_down="🔻"

percen_change_in_price = round((difference_in_value/yesterday_closing_price)*100)
print(percen_change_in_price)

if abs(percen_change_in_price)<5:
    response2 = requests.get(NEWS_ENDPOINT,news_params)
    articles = response2.json()["articles"]

three_articles = articles[:3]
print(articles)

formatted_articles = [f"{STOCK_NAME}: {up_down}{percen_change_in_price}%\nheadline:{article['title']}.\nbrief: {article['description']}" for article in three_articles]
print(formatted_articles)

client = Client(account_sid, auth_token)
for article in formatted_articles:
    message = client.messages.create(
        body= article,
        from_='+17472985992',
        to='+91 8448071122')
        


   

