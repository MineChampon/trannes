from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_test, name='post_test'),
    path('account/create/', views.account_create, name='account_create'),
    path('login/', views.login, name='login'),
]