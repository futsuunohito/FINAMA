from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Pendapatan
#@login_required
def income(request):
    return render(request, 'pendapatan/pendapatan.html')
