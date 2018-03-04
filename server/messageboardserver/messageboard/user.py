from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def user(request):
    if request.method == 'GET':
        data = {
            'name': 'lrh',
            'age': 18,
            'type': 'GET'
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    elif request.method == 'POST':
        data = {
            'name': 'lrh',
            'age': 18,
            'type': 'POST'
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    elif request.method == 'PUT':
        data = {
            'name': 'lrh',
            'age': 18,
            'type': 'PUT'
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    elif request.method == 'DELETE':
        data = {
            'name': 'lrh',
            'age': 18,
            'type': 'DELETE'
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    
