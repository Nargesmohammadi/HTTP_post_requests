import requests

USERNAME = "casi"
TOKEN = "hkhui23vy4ubnj2ub4ui5jkkh8ooe7940hn684bu3639jf"

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
    "id": "graph1",
    "name": "Reading Graph",
    "until": "h",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_end, json=graph_config, headers=headers)
print(response.text)