"""FINAMA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from Desk import views

app_name = 'Desk'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

    # Dashboard
    path('', views.index, name='index'),

    # Pendapatan
    path('income/', views.income, name='pendapatan'),

    # Pengeluaran
    path('expense/', views.expense, name='pengeluaran'),

    # Input Barang
    path('warehouse/', views.warehouse, name='input_barang'),

    # Data Piutang
    path('claim/', views.claim, name='data_piutang'),
]
