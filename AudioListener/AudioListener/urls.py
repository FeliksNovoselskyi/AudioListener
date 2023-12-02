"""
URL configuration for AudioListener project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

import Main.views as main_views
import Tracks.views as tracks_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.main_func, name='main_page'),
    path('tracks/', tracks_views.tracks_func, name='tracks_page'),
    path('phonk/', tracks_views.phonk_func, name='phonk_page'),
    path('rock/', tracks_views.rock_func, name='rock_page'),
    path('jazz/', tracks_views.jazz_func, name='jazz_page'),
    path('heavy_metal/', tracks_views.heavy_metal_func, name='heavy_metal_page'),
    path('classic/', tracks_views.classic_func, name='classic_page'),
]
