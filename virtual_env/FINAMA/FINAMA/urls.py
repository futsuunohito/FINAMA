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

from Desk.views import views_auth, views_dashboard, views_income, views_warehouse, views_expense, views_claim

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('register/', views_auth.user_register, name='register'),
    path('', views_auth.user_login, name='login'),
    path('logout/', views_auth.user_logout, name='logout'),

    # Dashboard
    path('dashboard/', views_dashboard.index, name='index'),

    # Pendapatan
    path('income/', views_income.income, name='pendapatan'),
    path('income/input', views_income.input, name='input_pendapatan'),
    path('income/update', views_income.update, name='update_pendapatan'),
    path('income/delete/<id>', views_income.delete, name='delete_pendapatan'),

    # Pengeluaran
    path('expense/', views_expense.expense, name='pengeluaran'),
    path('expense/input', views_expense.input, name='input_pengeluaran'),
    path('expense/update', views_expense.update, name='update_pengeluaran'),
    path('expense/delete/<id>', views_expense.delete, name='delete_pengeluaran'),

    # Input Barang
    path('warehouse/', views_warehouse.warehouse, name='barang'),
    path('warehouse/input', views_warehouse.input, name='input_barang'),
    path('warehouse/update', views_warehouse.update, name='update_barang'),
    path('warehouse/delete/<id>', views_warehouse.delete, name='delete_barang'),

    # Data Piutang
    path('claim/', views_claim.claim, name='piutang'),
    path('claim/input', views_claim.input, name='input_piutang'),
    path('claim/update', views_claim.update, name='update_piutang'),
    path('claim/delete/<id>', views_claim.delete, name='delete_piutang'),
]
