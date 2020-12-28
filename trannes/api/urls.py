from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('account/create/', views.account_create, name='account_create'),
    path('account/delete/', views.account_delete, name='account_delete'),
    path('account/detail/', views.account_detail, name='account_detail'),
]