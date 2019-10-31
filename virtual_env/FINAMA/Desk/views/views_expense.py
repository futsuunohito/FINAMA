from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Pengeluaran
#@login_required
def expense(request):
    return render(request, 'pengeluaran/pengeluaran.html')
