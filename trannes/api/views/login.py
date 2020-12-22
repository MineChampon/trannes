# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json


def login(request):
    result = 'true'

    if 'user_id' in request.POST:
        pass



    status = {
        "AccountCreateStatus": result,
    }
    
    response = json.dumps(status, ensure_ascii=False, indent=2) 
    return HttpResponse(response)
