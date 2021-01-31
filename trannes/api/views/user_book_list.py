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


def user_book_list(request):

    status = {
        "status": "false",
        "message": "本の取得に失敗しました"
    }
    

    try:
        if request.method == 'POST':
            post_data = json.loads(request.body)
            user_id = post_data["user_id"]
            
            isbn = []
            title = []

            userbooks = UserBooks.objects.values('isbn_id').filter(user_id=user_id)
            print(str(userbooks))
            for book_title in userbooks:
                print(book_title["isbn_id"])
                isbn.append(book_title["isbn_id"])
                book = Books.objects.values('book_title').filter(isbn_id=book_title["isbn_id"])
                title.append(book[0]["book_title"])
            

            status["status"] = "true"
            status["message"] = "追加された本を取得しました"
            status["isbn"] = isbn
            status["IsbnBookTitle"] = dict(zip(isbn, title))


    except:
        import traceback
        traceback.print_exc()

    finally:

        response = json.dumps(status, ensure_ascii=False, indent=2)
        return HttpResponse(response)