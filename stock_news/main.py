import os
import requests
import re
from twilio.rest import Client

CLEANR = re.compile('<.*?>')

MY_NUM = "+111222333"
TWILIO_NUM = "+333222111"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def check_stock_change(stock: str) -> float:
    """Returns stock change rate in percentages"""
    # Get stock data for the last two days
    alpha_url = "https://www.alphavantage.co/query"
    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": stock,
        "apikey": os.environ.get("ALPHA_API_KEY"),
    }
    response = requests.get(url=alpha_url, params=parameters)
    response.raise_for_status()
    stock_data = response.json()["Time Series (Daily)"]
    # Get closing prices for last two days
    last_two_close_prices = [float(value["4. close"]) for value in list(stock_data.values())[:2]]

    # Calculate change
    change = last_two_close_prices[0] - last_two_close_prices[1]
    change_rate = round(change / last_two_close_prices[0] * 100, 2)
    return change_rate


def get_news(keyword: str) -> list:
    """Return list of articles found for given keyword"""
    news_url = "https://newsapi.org/v2/everything"
    parameters = {
        "q": keyword,
        "searchIn": "title,content",
        "language": "en",
        "sortBy": "popularity",
        "apiKey": os.environ.get("NEWS_API_KEY"),
    }
    response = requests.get(url=news_url, params=parameters)
    response.raise_for_status()
    data = response.json()["articles"]
    return data


def prepare_message(stock_name: str, change_rate: float, article_dict: dict) -> str:
    """Prepares message to be sent via sms based on given article dict"""
    if change_rate >= 0:
        message = f"{stock_name}: 🔺{change_rate}%\n"
    else:
        message = f"{stock_name}: 🔻{change_rate * (-1)}%\n"

    title = re.sub(CLEANR, "", article_dict["title"])
    brief = re.sub(CLEANR, "", article_dict['description'])
    message += f"Headline: {title}\nBrief: {brief}"
    print(message)
    return message


def send_sms(text: str):
    """Sends sms containing given text using Twilio API"""
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=text,
                                     from_=TWILIO_NUM,
                                     to=MY_NUM)
    print(message.status)


stock_change = check_stock_change(STOCK)
if stock_change <= -5 or stock_change >= 5:
    articles = get_news(keyword=COMPANY_NAME)
    for article in articles[:3]:
        sms_message = prepare_message(STOCK, stock_change, article)
        send_sms(sms_message)
