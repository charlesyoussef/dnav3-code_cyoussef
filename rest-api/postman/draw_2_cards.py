import requests
from pprint import pprint

url = "https://deckofcardsapi.com/api/deck/yweb4z5mq4mr/draw/"

querystring = {"count":"2"}

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "ccc0b78f-aa9f-475a-a380-eb429dd34ac3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

pprint(response.text)