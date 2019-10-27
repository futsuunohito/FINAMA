from django.shortcuts import render

# Pengeluaran
def expense(request):
    return render(request, 'pengeluaran/pengeluaran.html')
