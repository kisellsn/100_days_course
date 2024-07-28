import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
APP_KEY = os.getenv("APP_KEY")

# TODO - get exersice info from user input

HOST_DOMAIN = "https://trackapi.nutritionix.com"
headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": APP_KEY,
}

exercise_endpoint = f"{HOST_DOMAIN}/v2/natural/exercise"

text = input("Enter your exercise: ")
WEIGHT = os.getenv("WEIGHT")
HEIGHT = os.getenv("HEIGHT")
AGE = os.getenv("AGE")
exercise_params = {
    "query": text,
    "weight_kg": float(WEIGHT),
    "height_cm": float(HEIGHT),
    "age": AGE
}
response = requests.post(exercise_endpoint, headers=headers, json=exercise_params)
exercises = response.json()["exercises"]
print(exercises)


# TODO: add row to Google Sheet using Sheety

# FIXME:
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}
PROJECT_NAME = "workoutsTracking"
USERNAME = os.getenv("USERNAME")
# USERNAME = os.environ.get("USERNAME", "couldn`t find the USERNAME")
sheety_endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/workouts"

date_field = datetime.date.today().strftime("%d-%m-%Y")
time_field = datetime.datetime.now().strftime("%H:%M:%S")

for exercise in exercises:
    sheety_params = {
        "workout": {
            "date": date_field,
            "time": time_field,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(sheety_endpoint, json=sheety_params, headers=sheety_headers)
    response.raise_for_status()
    print(response)

# delete_endpiont = "https://api.sheety.co/fa1a227a01b05e4892cdcea91e1705b7/workoutsTracking/workouts/2"
# response = requests.delete(delete_endpiont, headers=sheety_headers)


