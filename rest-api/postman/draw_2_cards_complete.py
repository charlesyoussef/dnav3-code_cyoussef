import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

querystring = {"deck_count":"6"}

headers = {
    'cache-control': "no-cache",
    'Postman-Token': "6b31b7eb-5621-41d3-b0b7-f4919601319c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
deck = response.json()
deck_id = deck["deck_id"]

# response_dict = json.loads(response.content)

# deck_id = response_dict["deck_id"]

print("The deck_id is: " + deck_id)


url2 = "https://deckofcardsapi.com/api/deck/{}/draw/".format(deck_id)

querystring2 = {"count":"4"}

headers2 = {
    'cache-control': "no-cache",
    'Postman-Token': "6105bb1b-711c-49ee-ada3-ae8d34049790"
    }

response2 = requests.request("GET", url2, headers=headers2, params=querystring2)

print(response2.text)
print(type(response2))