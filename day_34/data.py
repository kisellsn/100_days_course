import requests

amount = 5
type = "boolean"
params = {
    "amount": amount,
    "type": type,
}

response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()

data = response.json()
question_data = data["results"]
