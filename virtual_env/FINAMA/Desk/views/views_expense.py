from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_expenses import inputForm


# Pengeluaran
@login_required
def expense(request):
    return render(request, 'pengeluaran/pengeluaran.html')
   
def input(request):
    if request.method == 'POST':
        form = inputForm(request.POST)
    else :
        form = inputForm()
    
    context = {
        'form' : form
    }
    return render(request, 'pengeluaran/input.html', context)

def update(request):
    return render(request, 'pengeluaran/input.html')

def delete(request):
    return render(request, 'pengeluaran/pengeluaran.html')
