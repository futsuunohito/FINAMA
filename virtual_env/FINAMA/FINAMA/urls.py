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

from Desk.views import views_auth, views_dashboard, views_income
from Desk.views import views_warehouse, views_expense, views_claim

app_name = 'Desk'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('register/', views_auth.register, name='register'),
    path('login/', views_auth.login, name='login'),

    # Dashboard
    path('', views_dashboard.index, name='index'),

    # Pendapatan
    path('income/', views_income.income, name='pendapatan'),

    # Pengeluaran
    path('expense/', views_expense.expense, name='pengeluaran'),

    # Input Barang
    path('warehouse/', views_warehouse.warehouse, name='input_barang'),

    # Data Piutang
    path('claim/', views_claim.claim, name='data_piutang'),
]
