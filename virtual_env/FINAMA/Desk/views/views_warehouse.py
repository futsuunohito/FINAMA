from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_warehouse import inputForm
from django.contrib import messages
from Desk.models import Barang

# Input Barang
@login_required
def warehouse(request):
    barang = Barang.objects.all().order_by("-created_at")
    context = {
        'barang' : barang
    }
    return render(request, 'barang/barang.html', context)

def input(request):
    if request.method == 'POST':
        form = inputForm(request.POST)
        
        if form.is_valid():
            data = form.save(commit=False)
            data.id_accountant = request.user
            if Barang.objects.filter(nama_barang=data.nama_barang).exists():
                messages.warning(request, "Ditemukan barang dengan nama yang sama")
                return redirect("input_barang")
            data.save()
            warehouse(request)
            messages.success(request, 'Data barang berhasil dimasukan')
        else :
            messages.warning(request, 'Data barang gagal dimasukan')
            return render(request, 'barang/input.html')
        return redirect("barang")
    else :
        form = inputForm()
    
    context = {
        'form' : form
    }
    return render(request, 'barang/input.html', context)

def update(request, id):
    barang = Barang.objects.get(id_barang=id)
    form = inputForm(request.POST or None, instance=barang)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data barang berhasil disunting')
        return redirect("barang")
    context = {
        'form'  : form
    }
    return render(request, 'barang/update.html', context)

def delete(request, id):
    Barang.objects.get(id_barang = id).delete()
    messages.success(request, 'Data barang berhasil dihapus')
    return redirect("barang")
