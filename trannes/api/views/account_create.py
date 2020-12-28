# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

import datetime
import json
import hashlib, binascii

from ..models import *

def duplicate_and_element_check(json_datas):
    duplicate_check = "(" + json_datas["user_id"] + ")"
    if duplicate_check not in str(Users.objects.all()) and len(json_datas) == 6:
        return True
    else:
        return False

def account_create(request):

    status = {
        "status": "false",
        "message": "アカウントの作成に失敗しました"
    }

    try:
        if request.method == 'POST' and duplicate_and_element_check(json.loads(request.body)):
            post_data = json.loads(request.body) # POSTされたjsonデータ
            print(json.dumps(post_data, ensure_ascii=False, indent=2))
            
            #DB登録
            users = Users(
                        user_id = post_data["user_id"],
                        password = hashlib.sha256(post_data["password"].encode('utf-8')).hexdigest()
                    )

            userdetails = UserDetails(
                                user_id=post_data["user_id"],
                                user_name = post_data["user_name"],
                                mail_address = post_data["mail_address"],
                                gender = post_data["gender"],
                                birthday = post_data["birthday"],
                          )

            users.save()
            userdetails.save()

            #登録完後の処理
            status["status"] = "true"
            status["message"] = "アカウントが作成されました"
            status["PostData"] = post_data
            
        else:
            status["message"] = "そのIDは使用されています"
            if request.method == 'POST':
                print(json.dumps(json.loads(request.body), ensure_ascii=False, indent=2))

    except:
        import traceback
        traceback.print_exc()

    finally:
        #print(Users.objects.all())
        response = json.dumps(status, ensure_ascii=False, indent=2)
        return HttpResponse(response)