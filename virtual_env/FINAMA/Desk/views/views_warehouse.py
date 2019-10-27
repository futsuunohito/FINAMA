from django.shortcuts import render

# Input Barang
def warehouse(request):
    return render(request, 'input_barang/input_barang.html')
