import requests
from datetime import datetime

API_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = 'shdgijn234sdfsdv32'
USERNAME = 'cantseeathing'

user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=API_ENDPOINT, json=user_parameters)
# print(response.text)

GRAPH_ENDPOINT = f'{API_ENDPOINT}/{USERNAME}/graphs'
GRAPH_ID = 'graph1'

graph_parameters = {
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'KM',
    'type': 'float',
    'color': 'sora'
}
headers = {
    'X-USER-TOKEN': TOKEN
}

# graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_parameters, headers=headers)
# print(graph_response.text)

PIXEL_ENDPOINT = f'{GRAPH_ENDPOINT}/{GRAPH_ID}'
pixel_parameters = {
    'date': '20220830',
    'quantity': '6.9',
}
# pixel_request = requests.post(url=PIXEL_ENDPOINT, json=pixel_parameters, headers=headers)
# print(pixel_request.text)

print(datetime.now())
today_date = datetime.now().strftime('%Y%m%d')
print(today_date)

UPDATE_ENDPOINT = f'{PIXEL_ENDPOINT}/{today_date}'
update_parameters = {
    'quantity': '4.20'
}
# update_response = requests.put(url=UPDATE_ENDPOINT, json=update_parameters, headers=headers)
# print(update_response.text)

DELETE_ENDPOINT = UPDATE_ENDPOINT

# delete_response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(delete_response.text)
