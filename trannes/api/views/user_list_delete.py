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


def user_list_delete(request):

    status = {
        "status": "false",
        "message": "リストの削除に失敗しました"
    }
    

    try:
        if request.method == 'POST':
            post_data = json.loads(request.body)
            user_id = post_data["user_id"]
            list_name = post_data["list_name"]

            userlists = UserLists.objects.filter(user_id=user_id,list_name=list_name)
            userlists.delete()

            status["status"] = "true"
            status["message"] = "リストの削除が完了しました"
            status["list_name"] = list_name


    except:
        import traceback
        traceback.print_exc()

    finally:

        response = json.dumps(status, ensure_ascii=False, indent=2)
        return HttpResponse(response)