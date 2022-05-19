import requests

enpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(enpoint, json={'product_id': 123})
print(get_response.json()) 