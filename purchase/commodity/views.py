from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from . import models
import json

# Create your views here.

def index(request):
    
    return render(request, 'commodity.html')

def commodity_show(request):
    total = models.commodity.objects.count()
    items = models.commodity.objects.values()
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


def commodity_delete(request):
    if request.is_ajax():        
        commodity_serial = request.GET.getlist('id[]')
        for i in range(len(commodity_serial)):
            models.commodity.objects.filter(commodity_serial=commodity_serial[i]).delete()
        data = {'ret': True}
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        raise Http404("Not Found")

def commodity_modify(request):
    if request.is_ajax():        
        commodity_serial = request.GET.get('id')
        print(commodity_serial)
        commodity_num = request.GET.get('num')
        commodity_price = request.GET.get('price')
        print(commodity_price)
        item = models.commodity.objects.get(commodity_serial=commodity_serial)
        item.commodity_num = commodity_num
        item.commodity_price = commodity_price
        item.save()
        data = {
            'ret': True,            
        }
 
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return Http404("Not Found")
