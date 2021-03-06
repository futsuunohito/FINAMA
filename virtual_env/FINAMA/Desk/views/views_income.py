from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_income import inputForm
from Desk.models import Pendapatan, Barang
import json
from django.contrib import messages

# Pendapatan
@login_required
def income(request):
    pendapatan = Pendapatan.objects.filter(id_accountant = request.user.id).order_by("-created_at")
    context = {
        "pendapatan" : pendapatan
    } 
    return render(request, 'pendapatan/pendapatan.html', context)

def input(request):
    barang = Barang.objects.filter(id_accountant = request.user.id)
    nama_barang_list = json.dumps([i.nama_barang for i in barang]) 
    
    if request.method == 'POST':
        form = inputForm(request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.id_accountant = request.user
            try:
                barang_sel = Barang.objects.get(nama_barang = form.cleaned_data["nama_barang"], id_accountant = request.user.id)
            except Barang.DoesNotExist:
                messages.warning(request, 'Barang tidak ditemukan')
                return redirect("input_pendapatan")
    
            newBarang = inputForm(request.POST or None, instance=barang_sel).save(commit=False)
            newJumlah = newBarang.jumlah_barang - data.jumlah_pembelian
            if (newJumlah < 0):
                messages.warning(request, 'Jumlah barang tidak cukup')
                return redirect("input_pendapatan")
            else:
                data.id_barang = barang_sel
                data.total_pendapatan = data.jumlah_pembelian * (newBarang.harga_jual - newBarang.harga_beli)
                data.save()
                newBarang.jumlah_barang = newJumlah
                newBarang.save()

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
    oldJumlah = pendapatan.jumlah_pembelian
    if pendapatan.id_accountant_id != request.user.id:
        messages.warning(request, 'Data pendapatan tidak ditemukan')
        return redirect("pendapatan")

    form = inputForm(request.POST or None, instance=pendapatan)
    
    if form.is_valid():
        data = form.save(commit = False)
        
        barang_sel = Barang.objects.get(nama_barang = data.nama_barang, id_accountant = request.user.id)
        newBarang = inputForm(request.POST or None, instance=barang_sel).save(commit=False)
        
        currentJumlah = data.jumlah_pembelian
        newJumlah = barang_sel.jumlah_barang + (oldJumlah - currentJumlah)
        
        if (newJumlah < 0):
            messages.warning(request, 'Jumlah barang tidak cukup')
            return redirect("pendapatan")
        
        data.total_pendapatan = data.jumlah_pembelian * ( newBarang.harga_jual - newBarang.harga_beli )
        data.save()
        newBarang.jumlah_barang = newJumlah
        newBarang.save()
        
        messages.success(request, 'Data pendapatan berhasil disunting')
        return redirect("pendapatan")
    context = {
        'form'  : form
    }
    return render(request, 'pendapatan/update.html', context)

def delete(request, id):
    pendapatan = Pendapatan.objects.get(id_pendapatan = id)
    if pendapatan.id_accountant_id != request.user.id:
        messages.warning(request, 'Data pendapatan tidak ditemukan')
        return redirect("pendapatan")  
        
    barang_sel = Barang.objects.get(nama_barang = pendapatan.nama_barang, id_accountant = request.user.id)
    newBarang = inputForm(request.POST or None, instance=barang_sel).save(commit=False)

    newBarang.jumlah_barang = newBarang.jumlah_barang + pendapatan.jumlah_pembelian
    newBarang.save()  
    pendapatan.delete()
    messages.success(request, 'Data pendapatan berhasil dihapus')
    return redirect("pendapatan")
