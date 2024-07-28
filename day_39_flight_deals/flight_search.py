import os

import requests


class FlightSearch:
    def __init__(self):
        self._api_key = os.environ.get("API_KEY")
        self._api_secret = os.environ.get("API_SECRET")
        self._token = self._get_new_token()

    def get_destination_code(self, city_name):
        city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        search_params = {
            "keyword": city_name.upper(),
            "include": "AIRPORTS",
            "max": 2
        }
        headers = {
            "Authorization": f"Bearer {self._token}",
        }
        response = requests.get(city_search_endpoint, headers=headers, params=search_params)

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code

    def _get_new_token(self):
        auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        auth_params = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        auth_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(auth_endpoint, headers=auth_headers, data=auth_params)
        response.raise_for_status()
        return response.json()["access_token"]

    def check_flights(self, origin_city_iata, destination_iata, adults, max_price, from_time, to_time=None):
        flight_search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        flight_params = {
            "originLocationCode": origin_city_iata,
            "destinationLocationCode": destination_iata,
            "departureDate": from_time,
            "returnDate": to_time,
            "adults": adults,
            "currencyCode": "PLN",
            "max": 10,
            "maxPrice": max_price,
        }
        headers = {
            "Authorization": f"Bearer {self._token}",
        }
        response = requests.get(flight_search_endpoint, headers=headers, params=flight_params)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()["data"]

