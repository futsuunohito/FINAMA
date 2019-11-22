from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_warehouse import inputForm


# Input Barang
@login_required
def warehouse(request):
    return render(request, 'input_barang/input_barang.html')

def input(request):
    if request.method == 'POST':
        form = inputForm(request.POST)
    else :
        form = inputForm()
    
    context = {
        'form' : form
    }
    return render(request, 'input_barang/input.html', context)

def update(request):
    return render(request, 'input_barang/input.html')

def delete(request):
    return render(request, 'input_barang/pendapatan.html')
