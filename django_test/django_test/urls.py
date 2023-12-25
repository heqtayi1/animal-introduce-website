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
    path('imageList', homepage_views.image_list_page),
    path('videoList', homepage_views.video_list_page),
    path('upload', homepage_views.upload),
    path('upload_image', homepage_views.upload_image),
    path('upload_video', homepage_views.upload_video),
    path('search_image', homepage_views.search_image),
    path('imageProcessing', homepage_views.imageProcessing),
    path('load_image', homepage_views.load_image),
    path('grayscale_image', homepage_views.grayscale_image),
    path('imageRecognition', homepage_views.imageRecognition),
    path('Recognize', homepage_views.Recognize),
    path('chartDisplay', homepage_views.chartDisplay),
    path('animal',homepage_views.animal_page),
]

