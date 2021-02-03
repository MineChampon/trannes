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

from ..models import *

import random, string

def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def book_recognition(request):

    status = {
        "status": "false",
        "message": "文字認識に失敗しました"
    }

    try:
        if request.method == 'POST':
            post_data = json.loads(request.body, strict=False)
            ocr = post_data['base64']

            img_binary = base64.b64decode(ocr)
            jpg=np.frombuffer(img_binary,dtype=np.uint8)
            img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)

            file_path = "./api/save/"+randomname(8)+".jpg"
            cv2.imwrite(file_path,img)

            json_path = "./bookshelf-f1667c065eeb.json"

            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_path # json_pathは、サービスアカウントキーのパス

            # Instantiates a client
            client = vision.ImageAnnotatorClient()

            # Loads the image into memory
            with io.open(file_path, 'rb') as image_file:
                content = image_file.read()

            image = vision.Image(content=content)

            # Performs label detection on the image file
            response = client.text_detection(image=image)
            response = client.document_text_detection(image=image)
            # print(response.full_text_annotation.text)

            res = response.full_text_annotation.text.splitlines()

            print(res)
            def shopping(url_name):

                shopping = title = BeautifulSoup(requests.get(url_name).content, "html.parser").find('div','rgHvZc').text.replace('書籍','').replace('完全版','').replace('’',' ').replace('♪',' ').replace('/',' ').replace(':',' ').replace('-',' ').replace('(',' ').replace(')',' ').replace('（',' ').replace('）',' ').replace('［',' ').replace('］',' ').replace('[',' ').replace(']',' ').replace('<',' ').replace('>',' ').replace('【',' ').replace('】',' ')
                
                return shopping

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

                authorname = BeautifulSoup(requests.get(url_name).content, "html.parser").find('div', class_='infobox ml10 mt10').find_all('a')
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
                try:
                    dst_path = './api/image/' + isbn +'.jpg'
                    if not os.path.exists(dst_path):
                        url = requests.get(url)
                        soup = BeautifulSoup(url.content, "html.parser")
                        img_url = soup.find_all('meta')
                        image = re.findall(r"https://www.kinokuniya.co.jp/images/goods/ar2/web/imgdata2/large/[0-9]{5}/[0-9]{10}.jpg", str(img_url))
                        if image:
                             pass
                        else:
                            image = ["https://www.kinokuniya.co.jp/images/parts/goods-list/no-phooto.jpg"]
                        with urllib.request.urlopen(image[0]) as web_file:
                            data = web_file.read()
                            with open(dst_path, mode='wb') as local_file:
                                local_file.write(data)

                except urllib.error.URLError as e:
                    print(e)

            res_title= []
            res_isbn= []


            for ocr_str in res:
                urlName = """
                https://www.google.com/search?q={}&source=lnms&tbm=bks&sa=X&ved=2ahUKEwj-8bawqY3tAhVlwYsBHWXuCe8Q_AUoAXoECAsQCw&biw=683&bih=656
                """.format(ocr_str)

                print(urlName)


                books = BeautifulSoup(requests.get(urlName).content, "html.parser").find('div','BNeawe vvjwJb AP7Wnd')

                if books:
                    books = books.text.replace('書籍','').replace('完全版','').replace('’',' ').replace('♪',' ').replace('/',' ').replace(':',' ').replace('-',' ').replace('(',' ').replace(')',' ').replace('（',' ').replace('）',' ').replace('［',' ').replace('］',' ').replace('[',' ').replace(']',' ').replace('<',' ').replace('>',' ').replace('【',' ').replace('】',' ')
                    urlName2 = "https://www.kinokuniya.co.jp/disp/CSfDispListPage_001.jsp?qs=true&ptk=01&q="+ str(books)
                    url = requests.get(urlName2)
                    soup = BeautifulSoup(url.content, "html.parser")
                    b = soup.find_all('h3', class_='heightLine-2')
                    urls = re.findall(r"https://www.kinokuniya.co.jp/f/dsg-01-[0-9]{13}", str(b))
                    if urls:
                        book = urls[0]

                        o = urlparse(book)
                        isbn = o.path[10:]
                        
                        isbn_id = isbn
                        book_title = title(book)
                        book_genre = genre_text(book)
                        book_author = ""
                        if authorname_text(book):
                            book_author = authorname_text(book)[0]
                        book_detail = instructions(book)
                        
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

                        #返す配列
                        res_title.append(book_title)
                        res_isbn.append(isbn_id)

                        if not Books.objects.filter(isbn_id=isbn_id).exists():
                            #画像保存
                            download_file(book, isbn)
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
                        

            status["status"] = "true"
            status["message"] = "文字認識が完了しました"
            status["BookTitle"] = res_title
            status["isbn"] = res_isbn
            status["IsbnBookTitle"] = dict(zip(res_isbn, res_title))

    except:
        import traceback
        traceback.print_exc()

    finally:
        #print(Users.objects.all())
        response = json.dumps(status, ensure_ascii=False, indent=2)
        return HttpResponse(response)