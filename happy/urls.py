"""happy URL Configuration

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
from app.views import delete2, home, cadastro, cadastro2, create, create2, edit, update, edit2, update2, delete, delete2, doacao

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/', cadastro, name='cadastro'),
    path('cadastro2/', cadastro2, name='cadastro2'),
    path('create/', create, name='create'),
    path('create2/', create2, name='create2'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('edit2/<int:pk>/', edit2, name='edit2'),
    path('update2/<int:pk>/', update2, name='update2'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('delete2/<int:pk>/', delete2, name='delete2'),
    path('doacao/', doacao, name='doacao'),
]
