# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def post_test(request):
    return render( request, 'api/post_test.html')

def account_create(request):
    result = 'true'

    if 'user_id' in request.POST:
        pass



    status = {
        "AccountCreateStatus": result,
    }
    
    response = json.dumps(status, ensure_ascii=False, indent=2) 
    return HttpResponse(response)

def login(request):
    pass
