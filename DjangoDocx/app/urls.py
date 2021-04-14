#______________________________________________APPS URLS_____________________________________________

from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    # AUTH URLS
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout')
]



