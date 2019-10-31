from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Input Barang
@login_required
def warehouse(request):
    return render(request, 'input_barang/input_barang.html')
