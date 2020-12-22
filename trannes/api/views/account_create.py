# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json

from ..models import Users 


def account_create(request):
    result = 'true'
    users = Users(user_id="mojimoji", password="admin")
    users.save()
    print(Users.objects.all())


    if 'user_id' in request.POST:
        print("uwwww")



    status = {
        "AccountCreateStatus": result,
    }
    
    response = json.dumps(status, ensure_ascii=False, indent=2) 
    return HttpResponse(response)
