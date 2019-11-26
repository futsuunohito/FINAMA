from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_claim import inputForm


# Data piutang
@login_required
def claim(request):
    return render(request, 'data_piutang/data_piutang.html')

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
    
    context = {
        'form' : form
    }
    return render(request, 'data_piutang/input.html', context)

def update(request):
    return render(request, 'data_piutang/input.html')

def delete(request):
    return render(request, 'data_piutang/pengeluaran.html')