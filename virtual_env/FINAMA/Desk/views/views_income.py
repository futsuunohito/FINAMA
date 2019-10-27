from django.shortcuts import render

# Pendapatan
def income(request):
    return render(request, 'pendapatan/pendapatan.html')
