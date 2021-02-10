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


def user_book_recommend(request):

    status = {
        "status": "false",
        "message": "おすすめの取得に失敗しました"
    }
    

    try:
        if request.method == 'POST':
            post_data = json.loads(request.body)
            #user_id = post_data["user_id"]
            #isbn_id = post_data["isbn_id"]


            books = Books.objects.all()
            print(books)
            

            recommend_1 = []
            recommend_1_img = []
            
            recommend_2 = []
            recommend_2_img = []

            recommend_3 = []
            recommend_3_img = []


            for i in range(0,3):
                ran1 = random.randrange(0, len(books)-1)
                recommend_1.append(books[ran1].isbn_id)
                recommend_1_img.append(books[ran1].book_image)

                ran2 = random.randrange(0, len(books)-1)
                recommend_2.append(books[ran2].isbn_id)
                recommend_2_img.append(books[ran2].book_image)

                ran3 = random.randrange(0, len(books)-1)
                recommend_3.append(books[ran3].isbn_id)
                recommend_3_img.append(books[ran3].book_image)




            status["status"] = "true"
            status["message"] = "おすすめの取得が完了しました"
            status["recommend_1"] = recommend_1
            status["recommend_1_img"] = recommend_1_img
            status["recommend_2"] = recommend_2
            status["recommend_2_img"] = recommend_2_img
            status["recommend_3"] = recommend_3
            status["recommend_3_img"] = recommend_3_img

            
    except:
        import traceback
        traceback.print_exc()

    finally:

        response = json.dumps(status, ensure_ascii=False, indent=2)
        return HttpResponse(response)