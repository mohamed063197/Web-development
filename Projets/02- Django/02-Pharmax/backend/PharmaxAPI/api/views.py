from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def index(request, *args, **kwargs):
    data=json.loads(request.body)
    print("------Request.Body")
    print(request.body)#data from client

    print("------Request.Headers")
    print(request.headers)

    print("------Request.content_type")
    print(request.content_type)

    print("------Request.GET")
    print(request.GET)

    print("------Request.POST")
    print(request.POST)
    pre_data = json.dump(data)

    data['headers'] = dict(request.headers)
    data['params'] = dict(request.params)
    data['post'] = dict(request.POST)
    data['content_type']= dict(request.content_type)

    #data['headers'] = dict(request.headers)
    #data['content_type'] = request.content_type
    return JsonResponse(data)