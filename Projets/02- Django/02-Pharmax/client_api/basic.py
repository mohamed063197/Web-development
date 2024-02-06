import requests
from urllib.parse import urlparse, parse_qs

endpoint = "http://127.0.0.1:8000/patient/api/"
get_or_post = 'post'

if get_or_post == 'get':
    endpoint += "?title=medicaments"
    response = requests.get(endpoint)
    if response.status_code == 200:
        # HTTP REQUEST -->(reponse.text) HTML (shoud JSON, XML)
        # REST API HTTP -->(reponse.json) JSON 
        print(response.json())
        print(response.status_code)
else:
    response = requests.post(endpoint, json = {'name':'name', 'username':'username1', 'password':'password', 'passwordC':'passwordC', 'phone': '0753300460', 'age':18})
    if response.status_code == 200:
        # HTTP REQUEST -->(reponse.text) HTML (shoud JSON, XML)
        # REST API HTTP -->(reponse.json) JSON 
        print(response.json())
        print(response.status_code)






