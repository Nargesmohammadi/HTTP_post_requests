import requests

pixela_end = "https://pixe.la//v1/users"
user_params = {
    "token": "",
    "username ": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_end, json=user_params)
print(response.text)