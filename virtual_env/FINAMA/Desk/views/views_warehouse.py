from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_warehouse import inputForm
from django.contrib import messages
from Desk.models import Barang

# Input Barang
@login_required
def warehouse(request):
    barang = Barang.objects.all()
    context = {
        'barang' : barang
    }
    return render(request, 'input_barang/input_barang.html', context)

def input(request):
    if request.method == 'POST':
        form = inputForm(request.POST)
        
        
        if form.is_valid():
            data = form.save(commit=False)
            data.id_accountant = request.user
            # print("Your form has successfull submitted by ", form.id_accountant)
            data.save()
            warehouse(request)
            messages.success(request, 'Data barang berhasil dimasukan')
        else :
            messages.warning(request, 'Data barang gagal dimasukan')
            return render(request, 'input_barang/input.html')
        return redirect("barang")
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
