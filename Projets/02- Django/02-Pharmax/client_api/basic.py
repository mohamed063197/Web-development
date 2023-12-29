import requests
from urllib.parse import urlparse, parse_qs

endpoint = "http://127.0.0.1:8000/medecine/api?title=Dafalgon"
#response = requests.get(endpoint)
parsed_url = urlparse(endpoint)
query_params = parse_qs(parsed_url.query)

# Récupérer la valeur du paramètre spécifique
param_value = query_params.get('title', [None])[0]
response = requests.get(endpoint)

#response = requests.post(endpoint, json = {'title':'Medicament1', 'desc':'Desc1', 'favorite':True})

print(response.json())#get jsont has modified on dict
print(response.status_code)
# HTTP REQUEST -->(reponse.text) HTML (shoud JSON, XML)
# REST API HTTP -->(reponse.json) JSON 