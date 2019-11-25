from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Desk.forms.forms_income import inputForm


# Pendapatan
@login_required
def income(request):
    return render(request, 'pendapatan/pendapatan.html')

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
    return render(request, 'pendapatan/input.html', context)

def update(request):
    return render(request, 'pendapatan/input.html')

def delete(request):
    return render(request, 'pendapatan/pendapatan.html')
