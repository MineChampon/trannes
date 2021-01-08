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
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import cgi
import cgitb
#import pymysql.cursors
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

from PIL import Image


from ..models import *


def book_detail(request):

    status = {
        "status": "false",
        "message": "情報取得に失敗しました"
    }

    try:
        if request.method == 'POST':
            post_data = json.loads(request.body) # POSTされたjsonデータ
            print(json.dumps(post_data, ensure_ascii=False, indent=2))

            book = Books.objects.get(isbn_id=post_data["isbn_id"])
            bookgenres = BookGenres.objects.values('book_genre').filter(isbn_id=post_data["isbn_id"])
            
            genres = []

            for genre in bookgenres:
                genres.append(genre["book_genre"])
            status["status"] = "true"
            status["message"] = "情報取得が完了しました"
            status["BookTitle"] = book.book_title
            status["BookAuthor"] = book.book_author
            status["BookDetail"] = book.book_detail
            status["BookGenres"] = genres
            status["isbn"] = post_data["isbn_id"]

    except:
        import traceback
        traceback.print_exc()

    finally:
        #print(Users.objects.all())
        response = json.dumps(status, ensure_ascii=False, indent=2)
        return HttpResponse(response)