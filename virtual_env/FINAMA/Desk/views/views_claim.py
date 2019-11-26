from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_claim import inputForm
from django.contrib import messages
from Desk.models import Piutang

# Data piutang
@login_required
def claim(request):
    piutang = Piutang.objects.all().order_by("-created_at")
    context = {
        'piutang' : piutang
    }
    return render(request, 'piutang/piutang.html', context)

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
            return render(request, 'piutang/input.html')
        return redirect("piutang")
    else :
        form = inputForm()
    
    context = {
        'form' : form
    }
    return render(request, 'piutang/input.html', context)

def update(request):
    return render(request, 'piutang/input.html')

def delete(request, id):
    Piutang.objects.get(id_piutang = id).delete()
    messages.success(request, 'Data piutang berhasil dihapus')
    return redirect("piutang")