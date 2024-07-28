import os
import time
from pprint import pprint
from dotenv import load_dotenv
import datetime

from day_39_flight_deals.flight_data import FlightData, find_cheapest_flight
from day_39_flight_deals.notification_manager import NotificationManager
from flight_search import FlightSearch
from data_manager import DataManager

load_dotenv()
MY_CITY = "Gdansk"

data_manager = DataManager()

flight_search = FlightSearch()
sheet_data = data_manager.destination_data
users_data = data_manager.users_data

notification_manager = NotificationManager()

# ---------------------------- IATA Code Search ---------------------------------- #
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ---------------------------- Cheapest Flights ---------------------------------- #
origin_city_iata = flight_search.get_destination_code(MY_CITY)
departure_date = datetime.date.today() + datetime.timedelta(days=13)

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_iata,
        destination["iataCode"],
        adults=1,
        max_price=destination["lowestPrice"],
        from_time=departure_date,
    )
    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A":
        print(f"{destination['city']}: PLN {cheapest_flight.price}")
        is_direct = "direct" if cheapest_flight.is_direct else "indirect"
        text = (f"Low price alert! Only {cheapest_flight.price} PLN to {is_direct} fly from "
                f"{cheapest_flight.departure_city_code} to {cheapest_flight.destination_city_code}, "
                f"on {cheapest_flight.departure_date}")

        notification_manager.send_sms(
            message_body=text
        )

        notification_manager.send_email(
            email_list=users_data,
            email_body=text
        )

    time.sleep(2)
