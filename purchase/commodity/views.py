from django.shortcuts import render
from django.shortcuts import render
from . import models
import json

# Create your views here.

def commodity(request):
    items = models.commodity.objects.values()
    return render(request, 'commodity.html', {'items': json.dumps(list(items))})
