import datetime as dt
import os

from dotenv import load_dotenv
from newsapi import NewsApiClient
import requests
from twilio.rest import Client

load_dotenv()

STOCK = "T"
COMPANY_NAME = "AT&T Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ['STOCK_API_KEY']

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ['NEWS_API_KEY']

AUTH_TOKEN = os.environ['AUTH_TOKEN']
SID = os.environ['SID']
TWILIO_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']
MY_PHONE_NUMBER = os.environ['MY_PHONE_NUMBER']

newsapi = NewsApiClient(api_key=NEWS_API_KEY)


def get_news():
    company_articles = newsapi.get_everything(q=COMPANY_NAME,
                                              language='en',
                                              sort_by='publishedAt',
                                              page=1,
                                              page_size=3)
    return company_articles['articles']


def is_price_changed():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    stock_data = response.json()["Time Series (Daily)"]
    data_list = [day_data for key, day_data in stock_data.items()]

    yesterday_close_price = float(data_list[0]["4. close"])
    day_before_yesterday_close_price = float(data_list[1]["4. close"])

    difference = yesterday_close_price - day_before_yesterday_close_price

    diff_percent = abs(difference / yesterday_close_price * 100)
    if diff_percent < 5:
        news = get_news()
        if difference == abs(difference):
            text = make_text(news, "up", diff_percent)
        else:
            text = make_text(news, "down", diff_percent)
        return text
    return None


# TODO -. rfergogkdkg

def make_text(articles, direction, percent):
    direction = "🔺" if direction == "up" else "🔻"
    articles_text = [(f"{COMPANY_NAME} {direction}{round(percent, 2)}%\n\n"
                     f"Headline: {article['title']}\n"
                     f"Brief: {article['content']}") for article in articles]
    return articles_text


def send_news(articles):
    client = Client(SID, AUTH_TOKEN)
    for article in articles:
        message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            to=MY_PHONE_NUMBER,
            body=article
        )


text = is_price_changed()
if text:
    send_news(text)

