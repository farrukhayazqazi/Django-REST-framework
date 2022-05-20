import requests

enpoint = "http://127.0.0.1:8000/api/products/1/"

get_response = requests.post(enpoint, json={'title': 'Random title', 'content': 'Hello World'})
print(get_response.json())  