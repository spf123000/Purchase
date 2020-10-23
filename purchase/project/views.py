from django.shortcuts import render
from . import models

# Create your views here.
def project(request):
    projects = models.project.objects.values()
    return render(request, 'project.html', {'projects':projects})
