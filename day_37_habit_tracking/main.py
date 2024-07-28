import datetime
import os
import dotenv
import requests
from dotenv import load_dotenv

#https://pixe.la/v1/users/kisellsn/graphs/code0.html


pixela_endpoint = "https://pixe.la/v1/users"

load_dotenv()
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

headers = {
    "X-USER-TOKEN": TOKEN
}
# TODO 1 Create user

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

# TODO 2 Create graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "code0"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# TODO 3 Put some data
coding_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.date.today().strftime("%Y%m%d")
coding_session_params = {
    "date": today,
    "quantity": input("How many minutes did you get today for coding? "),
}

response = requests.post(coding_graph_endpoint, json=coding_session_params, headers=headers)
print(response.text)

# TODO 4 Update data
update_date = today
update_endpoint = f"{coding_graph_endpoint}/{update_date}"
update_params = {
    "quantity": input("How many minutes did you get for coding? "),
}
# response = requests.put(update_endpoint, json=update_params, headers=headers)
# print(response.text)

# TODO 5 Delete data

delete_date = today
delete_endpoint = f"{coding_graph_endpoint}/{delete_date}"

# response = requests.delete(delete_endpoint, headers=headers)
# print(response.text)
