from django.shortcuts import render
from django.shortcuts import render
from . import models
import json

# Create your views here.

def commodity(request):
    if request.is_ajax() and request.method == "POST":
        pass




    items = models.commodity.objects.values()
    return render(request, 'commodity.html', {'items': json.dumps(list(items))})

def commodity_save(request):
    if request.is_ajax():
        commodity_id = request.GET.getlist