from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client


load_dotenv()
WEATHER_API_KEY = os.environ['WEATHER_API_KEY']

AUTH_TOKEN = os.environ['AUTH_TOKEN']
SID = os.environ['SID']
TWILIO_PHONE_NUMBER = os.environ['TWILIO_PHONE_NUMBER']
MY_PHONE_NUMBER = os.environ['MY_PHONE_NUMBER']

MY_LAT = 54.227734
MY_LONG = 18.626517

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"


def will_rain():
    params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": WEATHER_API_KEY
    }
    response = requests.get(
        url=OWM_endpoint,
        params=params
    )
    response.raise_for_status()
    data = response.json()
    three_hours_weather_list = data["list"]

    if any(x["weather"][0]["id"] < 700 for x in three_hours_weather_list):
        return True

    return False


if will_rain():
    client = Client(SID, AUTH_TOKEN)
    message = client.messages.create(
        from_=TWILIO_PHONE_NUMBER,
        to=MY_PHONE_NUMBER,
        body="Bring the umbrella!☂️"
    )

    print(message.status)
