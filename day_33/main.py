import time

import requests
import datetime as dt
import smtplib

EMAIL = "sonyakondratskaya@gmail.com"
PASSWORD = "ereo ozya axce vkqp"
MY_LAT = 50.503830
MY_LONG = 17.418350


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5


def is_dark():
    my_location = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="http://api.sunrise-sunset.org/json", params=my_location)
    response.raise_for_status()
    data = response.json()

    sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = dt.datetime.now()

    return int(sunset_hour) < time_now.hour < int(sunrise_hour)

while True:
    if is_iss_overhead() and is_dark():
        time.sleep(60*60)
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(user=EMAIL, password=PASSWORD)
            server.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:LOOK UP!\n\n"
                                f"The iss is above you in the sky")
