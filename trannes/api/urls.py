from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('account/create/', views.account_create, name='account_create'),
]