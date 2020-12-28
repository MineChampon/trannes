# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

import datetime
import json
import hashlib, binascii

from ..models import *

def password_match_check(json_datas):
    registered_password = Users.objects.get(user_id = json_datas["user_id"]).password
    post_password = hashlib.sha256(json_datas["password"].encode('utf-8')).hexdigest()
    if registered_password == post_password:
        return True
    else:
        return False

def login(request):

    status = {
        "status": "false",
        "message": "ログインに失敗しました"
    }

    try:
        if request.method == 'POST' and password_match_check(json.loads(request.body)):
            post_data = json.loads(request.body) # POSTされたjsonデータ
            print(json.dumps(post_data, ensure_ascii=False, indent=2))

            status["status"] = "true"
            status["message"] = "ログインに成功しました"
            status["PostData"] = post_data

        else:
            status["message"] = "パスワードが一致しません"
            if request.method == 'POST':
                print(json.dumps(json.loads(request.body), ensure_ascii=False, indent=2))

    except:
        import traceback
        traceback.print_exc()

    finally:
        response = json.dumps(status, ensure_ascii=False, indent=2)
        return HttpResponse(response)