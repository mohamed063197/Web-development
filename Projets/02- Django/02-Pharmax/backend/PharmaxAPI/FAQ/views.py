from .models import FAQ
from medecine.models import Medecine

from .serializer import FAQSerializer
import json
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.shortcuts import get_object_or_404, render,redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view




# Create your views here.

@api_view(['POST','GET'])
def api(request, m):#request : le resultat de requests.get("url_nav")

    if request.method == 'GET':
        serialized_data = []
        data = []
        p_title = request.GET.get('title') 
        if not p_title:
            data = FAQ.objects.all().order_by('id')
        else:
            data = FAQ.objects.filter(title__iexact=p_title).order_by('id')
        for item in data:
            serialized_data.append(FAQSerializer(item).data)
        return Response(serialized_data)
    elif request.method == 'POST':
        print(request.data) #request.POST pour le formulaire et pour les requette api c'est request.data
        item = FAQ()
        errors = {}
        if not item.input_control(request.data.get('title'),
                                         request.data.get('desc'),
                                         request.data.get('online'),
                                         request.data.get('slug'),
                                         request.data.get('medecine'),
                                         request.data.get('desc_sound')):

            errors = item.get_errors_dict()
        else:
            if not item.db_input_control():
                errors = item.get_db_errors_dict()
            else:
                item.save()
                context = {
                    'item':FAQSerializer(item).data,
                    'errors':json.dumps({}),
                }
                
        context = {
            'item': FAQSerializer(item).data,
            'errors': json.dumps(errors),
        } 

        
        return Response(context)
    

"""
    INDEX
"""
def index(request, m):
    MEDECINE = get_object_or_404(Medecine, pk = m) 
    print(MEDECINE)

    data=[]
    if not request.GET.get('key_word'):
        data = FAQ.objects.filter(medecine=MEDECINE).order_by('id')
    else:
        data = FAQ.objects.filter(Q(medecine=MEDECINE) & Q(title__icontains=request.GET.get('key_word')) & Q(desc__icontains=request.GET.get('key_word'))).order_by('id')   
    try:
        paginator = Paginator(data, 10)# data, max_data_in_page
        page = request.GET.get('page',1)
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    return render(request, 'FAQ/index.html', {'data':data, 'search': request.GET.get('key_word'), 'count':paginator.count})

def add(request, m):
    MEDECINE = get_object_or_404(Medecine, pk = m)
    
    context={
        'item':None,
        'APP_NAME':FAQ().get_app_name(),
        'medecine':MEDECINE
    }
    if request.method== 'POST':
        item = FAQ()
        context=dict()
        if not item.input_control(request.POST.get('title'),
                                         request.POST.get('desc'),
                                         request.POST.get('online')=='on',
                                         request.POST.get('slug'),
                                         MEDECINE,
                                         request.POST.get('desc_sound')):

            errors = item.get_errors_dict()
        else:
            if not item.db_input_control():
                errors = item.get_db_errors_dict()
            else:
                item.save()
                context = {
                    'item':FAQ(),
                    'APP_NAME':FAQ().get_app_name(),
                    'medecine':MEDECINE,
                    'errors':{},
                }
                return render(request, 'FAQ/add.html', context)
        context = {
            'item': item,
            'APP_NAME':FAQ().get_app_name(),
            'medecine':MEDECINE,
            'errors': errors,
        } 

    return render(request, 'FAQ/add.html', context)

def delete(request, id=None):
    item = get_object_or_404(FAQ, pk = id) 
    item.delete()
    return redirect('FAQ:index')


"""
    UPDATE
"""
def update(request,m=None, id=None):
    MEDECINE = get_object_or_404(Medecine, pk = m)
    item = FAQ()
    context=dict()

    item = get_object_or_404(FAQ, pk = id) 
    context = {
        'item':item,
        'type':'update',
        'medecine':MEDECINE
    }    
    
    if request.method== 'POST':
        if not item.input_control(request.POST.get('title'),
                                         request.POST.get('desc'),
                                         request.POST.get('online')=='on',
                                         request.POST.get('slug'),
                                         request.data.get('medecine'),
                                         request.POST.get('desc_sound')):
            print(item.img.url)
            errors = item.get_errors_dict()
            context={
                'item':item,
                'medecine':MEDECINE,
                'errors':errors,
                'type':'update'
            }
        else:
            if not item.db_input_control(type='update'):
                errors = item.get_db_errors_dict()
                context={
                    'item':item,
                    'medecine':MEDECINE,
                    'errors':errors,
                    'type':'update'
                }
            else:
                item.save()
                errors= dict()
                
                return redirect('FAQ:index')
        context = {
            'item': item,
            'medecine':MEDECINE,
            'errors': errors,
            'type':'update'
        } 
    return render(request, 'FAQ/update.html', context)


def details(request, m=None, id=None):
    MEDECINE = get_object_or_404(Medecine, pk = m)
    item = FAQ()
    context=dict()

    item = get_object_or_404(FAQ, pk = id) 
    context = {
        'item':item,
        'medecine':MEDECINE,
        'type':'details'
    }    
    
    return render(request, 'FAQ/update.html', context)
