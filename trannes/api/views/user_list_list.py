# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse

import datetime
import json
import hashlib, binascii
import sys
import os
import io

import hashlib
import codecs
import requests
import base64
import cv2
import numpy as np
import random, string

from google.cloud import vision

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse
import urllib


from ..models import *


def user_list_list(request):

    status = {
        "status": "false",
        "message": "リスト情報の取得に失敗しました"
    }
    

    try:
        if request.method == 'POST':
            post_data = json.loads(request.body) # POSTされたjsonデータ
            print(json.dumps(post_data, ensure_ascii=False, indent=2))
            userlists = UserLists.objects.values('list_id', 'list_name').filter(user_id = post_data["user_id"])

            print(userlists)

            listId = []
            listName = []
            isbn_id = []

            for userlist in userlists:
                print(userlist)
                listId.append(userlist["list_id"])
                listName.append(userlist["list_name"])

                userslistbooks = UsersListBooks.objects.values('isbn_id').filter(list_id = userlist["list_id"])
                addisbn = []
                for userslistbook in userslistbooks:
                    addisbn.append(userslistbook["isbn_id"])
                isbn_id.append(addisbn)

            

            status["status"] = "true"
            status["message"] = "リスト情報を取得しました"
            status["list_id"] = listId
            status["list_name"] = listName
            status["isbn_id"] = isbn_id

    except:
        import traceback
        traceback.print_exc()

    finally:

        response = json.dumps(status, ensure_ascii=False, indent=2)
        return HttpResponse(response)