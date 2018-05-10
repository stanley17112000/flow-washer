"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from flow_washer.views import index
from flow_washer.views import checkPassword
from flow_washer.views import console
from flow_washer.views import addTask
from flow_washer.views import deleteTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('checkPassword/',checkPassword),
    path('console/', console),
    path('addTask/', addTask),
    path('deleteTask/', deleteTask)
]
