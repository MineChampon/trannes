# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def post_test(request):
    return render( request, 'api/post_test.html')

def createAccount(request):
    if 'user_id' in request.POST:
        result = 'true'
        params = {
            "createAccountResult": result,
        }
        json_str = json.dumps(params, ensure_ascii=False, indent=2) 
        return HttpResponse(json_str)

def login(request):
    if 'user_id' in request.POST:
        result = 'POST'
        params = {
            'user_id':result,
        }
        json_str = json.dumps(params, ensure_ascii=False, indent=2) 
        return HttpResponse(json_str)
