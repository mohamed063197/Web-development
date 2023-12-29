from .models import Medecine
from .forms import MedecineForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import MedecineSerializer

# Create your views here.

@api_view(['POST','GET'])
def api(request, *args, **kwargs):#request : le resultat de requests.get("url_nav")
    data = {}
    if request.method == 'GET':
        v_title = request.GET.get('title') 
        data=[]
        if v_title == None:
            query = Medecine.objects.all().order_by('id')
        else:
            query = Medecine.objects.filter(title=v_title).filter(favorite__exact=True).order_by('id')
        for medecine in query:
            data.append(MedecineSerializer(medecine).data)

    elif request.method == 'POST':
        #Traitement post
        data = request.data
    print(data)
    return Response(data)

def index(request):
    v_title = request.GET.get('title') 
    data=[]
    if v_title == None:
        query = Medecine.objects.all().order_by('id')
    else:
        query = Medecine.objects.filter(title__iexact=v_title).filter(favorite__exact=True).order_by('id')
    """
    exact: sensible a la case =
    iexact: insencible a la case 
    contains : like %%
    in : IN
    """    
    data = query

    return render(request, 'medecine/index.html', {'data':data})

def update(request):
    print(request.POST)
    
    medecine = Medecine()
    medecine.title = request.POST.get('title') 
    medecine.desc = request.POST.get('desc')
    medecine.slug = request.POST.get('slug')
    medecine.img = request.POST.get('img')
    medecine.favorite = request.POST.get('favorite') == 'on' 
    medecine.save()
    
    return render(request, 'medecine/update.html')