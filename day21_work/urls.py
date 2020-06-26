"""day21_work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path

from host import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', views.data),

    path('application/', views.application),
    path('del_app/', views.del_app),
    re_path('edit_app-(?P<p>\d+)/', views.edit_app),
    path('add_app/', views.add_app),

    path('bussiness/', views.bussiness),
    path('add_buss/', views.add_buss),
    re_path('edit_buss-(\d+)/', views.edit_buss),
    path('del_buss/', views.del_buss),

    path('host/', views.host),
    re_path("edit_host-(\d+)/", views.edit_host),

    path('login/', views.login),
]
