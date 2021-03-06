from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('account/create/', views.account_create, name='account_create'),
    path('account/delete/', views.account_delete, name='account_delete'),
    path('account/detail/', views.account_detail, name='account_detail'),
    
    path('book/recognition/', views.book_recognition, name='book_recognition'),
    path('book/detail/', views.book_detail, name='book_detail'),
    path('book/search/', views.book_search, name='book_search'),

    path('user/book/add/', views.user_book_add, name='user_book_add'),
    path('user/book/delete/', views.user_book_delete, name='user_book_delete'),
    path('user/book/list/', views.user_book_list, name='user_book_list'),
    path('user/book/search/', views.user_book_search, name='user_book_search'),
    path('user/book/recommend/', views.user_book_recommend, name='user_book_recommend'),

    path('user/list/create/', views.user_list_create, name='user_list_create'),
    path('user/list/delete/', views.user_list_delete, name='user_list_delete'),
    path('user/list/book/add/', views.user_list_book_add, name='user_list_book_add'),
    path('user/list/book/delete/', views.user_list_book_delete, name='user_list_book_delete'),
    path('user/list/list/', views.user_list_list, name='user_list_list'),


]