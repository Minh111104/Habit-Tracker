import requests
from datetime import datetime

USERNAME = "quangminhnguyen"
TOKEN = "boy111104"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"    # POST https://pixe.la/v1/users

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)    # create an account on Pixela

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"   # POST - /v1/users/<username>/graphs

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {                 # Authenticate myself (my account) using headers
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# today = datetime(year=2023, month=9, day=26)
# print(today.strftime("%Y%m%d"))
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you run today? "),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# HTTP Requests
# requests.get()
# requests.post()
# requests.put() will update a pixel
# requests.delete()

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "3.5"
}
# response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=update_endpoint,json=delete_endpoint,headers=headers)
# print(response.text)
