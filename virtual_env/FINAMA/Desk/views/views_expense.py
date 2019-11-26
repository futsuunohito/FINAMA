from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_expenses import inputForm
from django.contrib import messages
from Desk.models import Pengeluaran

# Pengeluaran
@login_required
def expense(request):
    pengeluaran  = Pengeluaran.objects.all()
    context = {
        "pengeluaran" : pengeluaran
    }
    return render(request, 'pengeluaran/pengeluaran.html', context)
   
def input(request):
    if request.method == 'POST':
        form = inputForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.id_accountant = request.user
            data.save()
            messages.success(request, 'Data pengeluaran berhasil dimasukan')
        else :
            messages.warning(request, 'Data pengeluaran gagal dimasukan')
            return render(request, 'pengeluaran/input.html')

        return redirect("pengeluaran")
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
