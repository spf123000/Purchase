from django.shortcuts import render
from django.shortcuts import render
from . import models

# Create your views here.

def commodity(request):
    items = models.commodity.objects.values()
    return render(request, 'commodity.html', {'items':items})
