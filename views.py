from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import requests
from .models import Diario
import json
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def lista(request):    
    diario = list(Diario.objects.values().all()) 
    return JsonResponse({'diario':diario}) 


def crear(request):
    try:
        datos = json.loads(request.body.decode('utf-8'))
        diario = Diario(sentimiento= datos['sentimiento'], descripcion= datos['descripcion'], 
            fecha = datos['fecha'], imagen = 'img/'+datos['imagen'])
        diario.save()
        ultimo = list(Diario.objects.filter(id = diario.pk).values().all())
        data = {'ultimo': ultimo}
    except IntegrityError:
        print("no se guardo")
        data = { 'valido' : False }
    return JsonResponse(data)    

