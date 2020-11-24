from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import commodity
from project.models import project 
from report.models import report
import json

# Create your views here.

def index(request):    
    return render(request, 'commodity.html')

def commodity_show(request):    
    total = commodity.objects.count()
    items = commodity.objects.values()
    rows = []
    for item in items:
        rows.append({
            'commodity_serial' : item['commodity_serial'],
            'commodity_id' : item['commodity_id'],
            'commodity_link' : item['commodity_link'],
            'commodity_name' : item['commodity_name'],
            'commodity_num' : item['commodity_num'],
            'commodity_price' : item['commodity_price'],
            'commodity_total' : item['commodity_total'],
        })
    data = {'total': total, 'rows': rows}
    # return render(request, 'commodity.html', data)
    return HttpResponse(json.dumps(data), content_type='application/json')

def commodity_show_options(request):
    projects = []
    # project_data = []
    results = project.objects.values()
    for result in results:
        # project_data.append({
        projects.append({
            'project_id': result['project_id'],
            'project_name': result['project_name'],
            'project_manager': result['project_manager'],
        })
    # projects = {'projects': project_data}
    # return render(request, 'commodity.html', {'projects': projects})
    return HttpResponse(json.dumps(projects), content_type='application/json')

def commodity_delete(request):
    if request.is_ajax():
        ids = request.GET.getlist('id[]')
        for i, j in enumerate(ids):
        # for i in range(len(commodity_serial)):
            commodity.objects.filter(commodity_serial=j).delete()
        data = {'ret': True}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404("Not Found")

def commodity_modify(request):
    if request.is_ajax():
        commodity_serial = request.GET.get('id')
        commodity_num = request.GET.get('num')
        commodity_price = request.GET.get('price')
        item = commodity.objects.filter(commodity_serial=commodity_serial)
        item.commodity_num = commodity_num
        item.commodity_price = commodity_price
        item.save()
        data = {
            'ret': True,
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return Http404("Not Found")

def commodity_submit(request):
    if request.is_ajax():
        ids = request.GET.getlist('ids[]')
        project_id = request.GET.get('project')
        project_item = project.objects.get(project_id=project_id)
        print(ids)
        for i, j in enumerate(ids):
            commodity_item = commodity.objects.get(commodity_serial=j)
            report(report_id=commodity_item.commodity_id,\
                report_link=commodity_item.commodity_link,\
                report_name=commodity_item.commodity_name,\
                report_num=commodity_item.commodity_num,\
                report_price=commodity_item.commodity_price,\
                report_project=project_item.project_name).save()
        data = {
            'ret': True,
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return Http404("Not Found")
