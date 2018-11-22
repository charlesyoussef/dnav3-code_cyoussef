import requests
from pprint import pprint

url = "https://api.ciscospark.com/v1/teams"

headers = {
    'Authorization': "Bearer NTlmZThkMmQtN2QwOS00OWVlLWJjYzMtYTNhMWVlOTdlOWFlMjlmN2Q2ZWQtZDRk",
    'cache-control': "no-cache",
    'Postman-Token': "f3b641a6-6a34-4482-8b42-533d2bbe5d0f"
    }

response = requests.request("GET", url, headers=headers)

pprint(response.text)
a = __file__
print(a)