"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage import views as homepage_views


urlpatterns = [
    path('', homepage_views.homepage),   #默认登录界面
    path('upload', homepage_views.upload),
    path('animal',homepage_views.animal_page),
    path('sound',homepage_views.sound_page),
    path('process_audio',homepage_views.process_audio),
    path('image_rec',homepage_views.image_rec),
    path('image_analyses',homepage_views.image_analyses)
    
]

