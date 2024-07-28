import os
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")

class DataManager:

    def __init__(self):
        self._sheety_token= os.getenv("SHEETY_TOKEN")
        self._sheety_headers = {
            "Authorization": f"Bearer {self._sheety_token}"
        }
        self.destination_data = self.get_destination_data()
        self.users_data = self.get_customer_emails()

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self._sheety_headers)
        data = response.json()
        return data["prices"]

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self._sheety_headers
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self._sheety_headers)
        data = response.json()
        return data["users"]