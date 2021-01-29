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


def book_search(request):

    status = {
        "status": "false",
        "message": "検索に失敗しました"
    }
    

    try:
        if request.method == 'POST':
            def title(url_name):

                title = BeautifulSoup(requests.get(url_name).content, "html.parser").find("h3").text
                
                return title

            def genre_text(url_name):

                genre = BeautifulSoup(requests.get(url_name).content, "html.parser").select('.pankuzu li')
                
                genre_text = []
                an = []
                
                for name in genre[1:]:
                    an.append(name.text.replace('>','').replace('\xa0','').replace('\n',"").replace('\u3000',""))
                    
                
                return an

            def authorname_text(url_name):
                
                authorname = BeautifulSoup(requests.get(url_name).content, "html.parser").find('div', class_='infobox ml10 mt10')
                authorname = authorname.find_all('a')
                authorname_text = []
                an = []
                for name in authorname[:-1]:
                    an.append(name.text)
                    
                return an

            def instructions(url_name): 

                instructions = BeautifulSoup(requests.get(url_name).content, "html.parser").find('div', class_='career_box').text.replace('\n', '\n\n')
                    
                bn = instructions.strip("\n")
                    
                return bn

            def download_file(url, isbn):
                urltext = ""
                try:
                    dst_path = './api/image/' + isbn +'.jpg'
                    if not os.path.exists(dst_path):
                        url = requests.get(url)
                        soup = BeautifulSoup(url.content, "html.parser")
                        img_url = soup.find_all('meta')
                        image = re.findall(r"https://www.kinokuniya.co.jp/images/goods/ar2/web/imgdata2/large/[0-9]{5}/[0-9]{10}.jpg", str(img_url))
                        if image:
                            urltext = str(image[0])
                            print(urltext)
                        else:
                            image = ["https://www.kinokuniya.co.jp/images/parts/goods-list/no-phooto.jpg"]
                            urltext = str(image[0])
                            print(urltext)
                        with urllib.request.urlopen(image[0]) as web_file:
                            data = web_file.read()
                            with open(dst_path, mode='wb') as local_file:
                                local_file.write(data)
                        

                except urllib.error.URLError as e:
                    print(e)

                return urltext

            post_data = json.loads(request.body)
            isbn_id = post_data["isbn_id"]
            book = "https://www.kinokuniya.co.jp/disp/CSfDispListPage_001.jsp?qs=true&ptk=01&q="+ str(isbn_id)
            o = urlparse(book)
            book_title = title(book)
            book_genre = genre_text(book)
            book_author = ""
            if authorname_text(book):
                book_author = authorname_text(book)[0]
            book_detail = instructions(book)
            download_file(book, isbn_id)

            book_image = ""

            url = requests.get(book)
            soup = BeautifulSoup(url.content, "html.parser")
            img_url = soup.find_all('meta')
            image = re.findall(r"https://www.kinokuniya.co.jp/images/goods/ar2/web/imgdata2/large/[0-9]{5}/[0-9]{10}.jpg", str(img_url))
            if image:
                book_image = str(image[0])
                print(book_image)
            else:
                image = ["https://www.kinokuniya.co.jp/images/parts/goods-list/no-phooto.jpg"]
                book_image = str(image[0])
                print(book_image)

            

            if not Books.objects.filter(isbn_id=isbn_id).exists():
                            #画像保存
                books = Books(
                            isbn_id = isbn_id,
                            book_title = book_title,
                            book_author = book_author,
                            book_detail = book_detail,
                            book_image = book_image
                        )
                books.save()

                for genre in book_genre:
                    bookgenres = BookGenres(
                                    isbn_id = isbn_id,
                                    book_genre = genre
                                )
                    bookgenres.save()
                    
            book = Books.objects.get(isbn_id=isbn_id)
            bookgenres = BookGenres.objects.values('book_genre').filter(isbn_id=isbn_id)
            genres = [] 
            for genre in bookgenres:
                genres.append(genre["book_genre"])

            status["status"] = "true"
            status["message"] = "検索が完了しました"
            status["BookTitle"] = book.book_title
            status["BookAuthor"] = book.book_author
            status["BookDetail"] = book.book_detail
            status["BookImage"] = book.book_image
            status["BookGenres"] = genres
            status["isbn"] = isbn_id


    except:
        import traceback
        traceback.print_exc()

    finally:

        response = json.dumps(status, ensure_ascii=False, indent=2)
        return HttpResponse(response)