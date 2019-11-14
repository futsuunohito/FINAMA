from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Pendapatan
@login_required
def income(request):
    return render(request, 'pendapatan/pendapatan.html')

def input(request):
    return render(request, 'pendapatan/input.html')

def update(request):
    return render(request, 'pendapatan/input.html')

def delete(request):
    return render(request, 'pendapatan/pendapatan.html')
