from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_claim import inputForm
from django.contrib import messages
from Desk.models import Piutang

# Data piutang
@login_required
def claim(request):
    piutang = Piutang.objects.all()
    context = {
        'piutang' : piutang
    }
    return render(request, 'data_piutang/data_piutang.html', context)

def input(request):
    if request.method == 'POST':
        form = inputForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.id_accountant = request.user
            data.save()
            messages.success(request, 'Data piutang berhasil dimasukan')
        else :
            messages.warning(request, 'Data piutang gagal dimasukan')
            return render(request, 'data_piutang/input.html')
        return redirect("data_piutang")
    else :
        form = inputForm()
    
    context = {
        'form' : form
    }
    return render(request, 'data_piutang/input.html', context)

def update(request):
    return render(request, 'data_piutang/input.html')

def delete(request):
    return render(request, 'data_piutang/data_piutang.html')