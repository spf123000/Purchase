from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import project
import json

# Create your views here.
def index(request):
    
    return render(request, 'project.html')

def project_add(request):
    if request.is_ajax():
        project_name = request.GET.get('name')
        project_manager = request.GET.get('manager')
        project(project_name=project_name, project_manager=project_manager).save()
        data = {'ret': True}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404("Not Found")

def project_show(request):
    total = project.objects.count()
    items = project.objects.values()
    rows = []
    for item in items:
        rows.append({
            'project_id' : item['project_id'],
            'project_name' : item['project_name'],
            'project_manager' : item['project_manager']
        })
    data = {'total': total, 'rows': rows}
    # return render(request, 'project.html', data)
    return HttpResponse(json.dumps(data), content_type='application/json')


def project_delete(request):
    if request.is_ajax():        
        project_id = request.GET.getlist('id[]')
        for i in range(len(project_id)):
            project.objects.filter(project_id=project_id[i]).delete()
        data = {'ret': True}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404("Not Found")

def project_modify(request):
    if request.is_ajax():        
        project_id = request.GET.get('id')
        # print(commodity_serial)
        project_name = request.GET.get('name')
        project_manager = request.GET.get('manager')
        # print(commodity_price)
        item = project.objects.get(project_id=project_id)
        item.project_name = project_name
        item.project_manager = project_manager
        item.save()
        data = {
            'ret': True,            
        }
 
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return Http404("Not Found")