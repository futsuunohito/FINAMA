from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_expenses import inputForm
from django.contrib import messages
from Desk.models import Pengeluaran

# Pengeluaran
@login_required
def expense(request):
    pengeluaran  = Pengeluaran.objects.all().order_by("-created_at")
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

def update(request, id):
    pengeluaran = Pengeluaran.objects.get(id_pengeluaran = id)
    form = inputForm(request.POST or None, instance=pengeluaran)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data pengeluaran berhasil disunting')
        return redirect("pengeluaran")

    context ={
        'form'  : form 
    }
    return render(request, 'pengeluaran/update.html', context)

def delete(request,id):
    Pengeluaran.objects.get(id_pengeluaran = id).delete()
    messages.success(request, 'Data pengeluaran berhasil dihapus')
    return redirect("pengeluaran")
