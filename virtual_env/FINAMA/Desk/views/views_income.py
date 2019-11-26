from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_income import inputForm
from Desk.models import Pendapatan, Barang
import json

# Pendapatan
@login_required
def income(request):
    pendapatan = Pendapatan.objects.all()
    context = {
        "pendapatan" : pendapatan
    } 
    return render(request, 'pendapatan/pendapatan.html', context)

def input(request):
    if request.method == 'POST':
        form = inputForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.id_accountant = request.user
            data.save()
        else :
            print("Invalid Form of Form")

    else :
        form = inputForm()

    nama_barang_list = json.dumps([i.nama_barang for i in Barang.objects.all()]) 
    context = {
        'form' : form,
        'nama_barang_list': nama_barang_list
    }
    return render(request, 'pendapatan/input.html', context)

def update(request):
    return render(request, 'pendapatan/input.html')

def delete(request):
    return render(request, 'pendapatan/pendapatan.html')
