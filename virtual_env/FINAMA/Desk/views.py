from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

# Dashboard with graphics
def index(request):
    return render(request, 'main.html')

# Pendapatan
def income(request):
    return render(request, 'pendapatan/pendapatan.html')

# Pengeluaran
def expense(request):
    return render(request, 'pengeluaran/pengeluaran.html')

# Input Barang
def warehouse(request):
    return render(request, 'input_barang/input_barang.html')

# Data piutang
def claim(request):
    return render(request, 'data_piutang/data_piutang.html')
