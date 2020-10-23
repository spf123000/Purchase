from django.shortcuts import render
from django.shortcuts import render
from . import models

# Create your views here.

def storage(request):
    items = models.storage.objects.values()
    return render(request, 'storage.html', {'items':items})
