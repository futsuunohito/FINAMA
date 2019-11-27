from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_income import inputForm
from Desk.models import Pendapatan, Barang
import json
from django.contrib import messages

# Pendapatan
@login_required
def income(request):
    pendapatan = Pendapatan.objects.all().order_by("-created_at")
    context = {
        "pendapatan" : pendapatan
    } 
    return render(request, 'pendapatan/pendapatan.html', context)

def input(request):
    barang = Barang.objects.all()
    nama_barang_list = json.dumps([i.nama_barang for i in barang]) 

    if request.method == 'POST':
        form = inputForm(request.POST)

        if form.is_valid():
            print(form)
            data = form.save(commit=False)
            data.id_accountant = request.user
            try:
                barang_sel = Barang.objects.get(nama_barang = form.cleaned_data["nama_barang"])
            except Barang.DoesNotExist:
                messages.warning(request, 'Barang tidak ditemukan')
                return redirect("input_pendapatan")
            data.id_barang = barang_sel
            data.save()
            messages.success(request, 'Data pendapatan berhasil dimasukan')
        else :
            messages.warning(request, 'Data pendapatan gagal dimasukan')
            return redirect("input_pendapatan")
        return redirect("pendapatan")

    else :
        form = inputForm()

    context = {
        'form' : form,
        'nama_barang_list': nama_barang_list
    }
    return render(request, 'pendapatan/input.html', context)

def update(request,id):
    pendapatan = Pendapatan.objects.get(id_pendapatan=id)
    form = inputForm(request.POST or None, instance=pendapatan)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data pendapatan berhasil disunting')
        return redirect("pendapatan")
    context = {
        'form'  : form
    }
    return render(request, 'pendapatan/update.html', context)

def delete(request, id):
    Pendapatan.objects.get(id_pendapatan = id).delete()
    messages.success(request, 'Data pendapatan berhasil dihapus')
    return redirect("pendapatan")
