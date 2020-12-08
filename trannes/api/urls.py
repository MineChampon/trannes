from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_test, name='post_test'),
    path('createAccount/', views.createAccount, name='createAccount'),
    path('login/', views.login, name='login'),
]