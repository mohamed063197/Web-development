from .models import Patient
from .serializer import PatientSerializer
import json
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.decorators import api_view

"""
   SINGIN
"""
@api_view(['POST','GET'])
def apiRegister(request):#request : le resultat de requests.get("url_nav")
    if request.method == 'POST':
        print(request.data) #request.POST pour le formulaire et pour les requette api c'est request.data
        item = Patient()
        errors = {}
        if not item.input_control_singIn(request.data.get('name'),
                                         request.data.get('username'),
                                         request.data.get('mail'),
                                         request.data.get('password'),
                                         request.data.get('passwordC'),
                                         request.data.get('phone'),
                                         request.data.get('age')):
            
            errors = item.get_errors_dict()
        else:
            if not item.db_input_control_singIn():
                errors = item.get_db_errors_dict()
            else:
                item.save()
                context = {
                    'item':PatientSerializer(item).data,
                    'errors':json.dumps({}),
                }
                
        context = {
            'item': PatientSerializer(item).data,
            'errors': json.dumps(errors),
        } 
        return Response(context)
    

"""
    LOGIN
"""
@api_view(['POST','GET'])
def apiLogin(request):#request : le resultat de requests.get("url_nav")
    if request.method == 'GET':
        serialized_data = []
        data = []

        if not item.input_control_login(request.GET.get('mail'),
                                        request.GET.get('password')):
            data = Patient.objects.all().order_by('id')
        else:
            data = Patient.objects.filter(mail__iexact = request.GET.get('mail')).order_by('id')
        
        for item in data:
            serialized_data.append(PatientSerializer(item).data)
        return Response(serialized_data)   
