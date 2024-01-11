import requests
from urllib.parse import urlparse, parse_qs

endpoint = "http://127.0.0.1:8000/medecine/api/"
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
    response = requests.post(endpoint, json = {'title':'pi', 'desc':'Desc mo', 'favorite':False, 'slug':'slug-mo'})
    if response.status_code == 200:
        # HTTP REQUEST -->(reponse.text) HTML (shoud JSON, XML)
        # REST API HTTP -->(reponse.json) JSON 
        print(response.json())
        print(response.status_code)






