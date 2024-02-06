from .models import Medecine
from .serializer import MedecineSerializer
import json
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.shortcuts import get_object_or_404, render,redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view

import logging

log = logging.getLogger('log')

# Create your views here.

@api_view(['POST','GET'])
def api(request, *args, **kwargs):#request : le resultat de requests.get("url_nav")

    if request.method == 'GET':
        serialized_data = []
        data = []
        p_title = request.GET.get('title') 
        if not p_title:
            data = Medecine.objects.all().order_by('id')
        else:
            data = Medecine.objects.filter(title__iexact=p_title).order_by('id')
        for item in data:
            serialized_data.append(MedecineSerializer(item).data)
        return Response(serialized_data)
    elif request.method == 'POST':
        print(request.data) #request.POST pour le formulaire et pour les requette api c'est request.data
        item = Medecine()
        errors = {}
        if not item.input_control(request.data.get('title'),
                                         request.data.get('desc'),
                                         request.data.get('online'),
                                         request.data.get('slug'),
                                         request.data.get('img')):

            errors = item.get_errors_dict()
        else:
            if not item.db_input_control():
                errors = item.get_db_errors_dict()
            else:
                item.save()
                context = {
                    'item':MedecineSerializer(item).data,
                    'errors':json.dumps({}),
                }
                
        context = {
            'item': MedecineSerializer(item).data,
            'errors': json.dumps(errors),
        }
        
        return Response(context)
    


def index(request):
    data=[]
    if not request.GET.get('key_word'):
        data = Medecine.objects.all().order_by('id')
    else:
        data = Medecine.objects.filter(Q(title__icontains=request.GET.get('key_word')) | Q(desc__icontains=request.GET.get('key_word'))).order_by('id')   
    try:
        paginator = Paginator(data, 5)# data, max_data_in_page
        page = request.GET.get('page',1)
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {
        'data':data, 
        'search': request.GET.get('key_word'), 
        'count':paginator.count,
        'PAGE_TITLE': 'MEDECINES',
        }
    
    return render(request, 'medecine/index.html', context)

def add(request):
    context={
        'item':None,
        'APP_NAME':Medecine().get_app_name(),
        'PAGE_TITLE': 'MEDECINES',
    }
    if request.method== 'POST':
        item = Medecine()
        context=dict()
        if not item.input_control(request.POST.get('title'),
                                         request.POST.get('desc'),
                                         request.POST.get('online')=='on',
                                         request.POST.get('slug'),
                                         request.POST.get('img')):

            errors = item.get_errors_dict()
        else:
            if not item.db_input_control():
                errors = item.get_db_errors_dict()
            else:
                item.save()
                context = {
                    'item':Medecine(),
                    'APP_NAME':Medecine().get_app_name(),
                    'errors':{},
                    'PAGE_TITLE': 'MEDECINES',
                }
                return render(request, 'medecine/add.html', context)
        context = {
            'item': item,
            'APP_NAME':Medecine().get_app_name(),
            'errors': errors,
            'PAGE_TITLE': 'MEDECINES',
        } 

    return render(request, 'medecine/add.html', context)

def delete(request, id=None):
    item = get_object_or_404(Medecine, pk = id) 
    item.delete()
    return redirect('medecine:index')

def update(request, id=None):
    item = Medecine()
    context=dict()

    item = get_object_or_404(Medecine, pk = id) 
    context = {
        'item':item,
        'type':'update',
        'PAGE_TITLE': 'MEDECINES',
    }    
    
    if request.method== 'POST':
        if not item.input_control(request.POST.get('title'),
                                         request.POST.get('desc'),
                                         request.POST.get('online')=='on',
                                         request.POST.get('slug'),
                                         request.POST.get('img')):
            print(item.img.url)
            errors = item.get_errors_dict()
            context={
                'item':item,
                'errors':errors,
                'type':'update',
                'PAGE_TITLE': 'MEDECINES',
            }
        else:
            if not item.db_input_control(type='update'):
                errors = item.get_db_errors_dict()
                context={
                    'item':item,
                    'errors':errors,
                    'type':'update',
                    'PAGE_TITLE': 'MEDECINES',
                }
            else:
                item.save()
                errors= dict()
                
                return redirect('medecine:index')
        context = {
            'item': item,
            'errors': errors,
            'type':'update',
            'PAGE_TITLE': 'MEDECINES',
        } 
    return render(request, 'medecine/update.html', context)


def details(request, id=None):
    item = Medecine()
    context=dict()

    item = get_object_or_404(Medecine, pk = id) 
    context = {
        'item':item,
        'type':'details',
        'PAGE_TITLE': 'MEDECINES',
    }    
    
    return render(request, 'medecine/update.html', context)
