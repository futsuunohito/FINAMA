from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'main.html')

def income(request):
    return render(request, 'pendapatan.html')

def expense(request):
    return render(request, 'pengeluaran.html')
