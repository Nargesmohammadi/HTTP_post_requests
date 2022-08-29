import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH = "graph1"
pixela_end = "https://pixe.la//v1/users"
user_params = {
    "token": TOKEN,
    "username ": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThisIsThanksCode"
}
# response = requests.post(url=pixela_end, json=user_params)
# print(response.text)
graph_end = f"{pixela_end}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
    "name": "Walking Graph",
    "until": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_end, json=graph_config, headers=headers)
# print(response.text)
pixel_creation_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPH}"

today = datetime(year=2022, month=8, day=29)


pixela_data = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many kilometer did you walk today?"),  # the time that I'm walking today.
}


update_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"

# new pixel data:
update_params = {
    "quantity": "3.5"
}

delete_end = f"{pixela_end}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"


# response = requests.put(url=update_end, json=update_params, headers=headers)
# print(response.text)

response = requests.delete(url=delete_end, headers=headers)
