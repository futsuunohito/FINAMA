from django.shortcuts import render
from Desk.forms.forms_auth import AccountantForm
from Desk.views.views_dashboard import index

from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
        
    if request.method == "POST":
        regist_form = AccountantForm(request.POST)

        if regist_form.is_valid():
            registrate = regist_form.save()
            registrate.set_password(registrate.password)
            registrate.save()

            return user_login(request)
        else:
            messages.error(request, "Registration Form Invalid")

    regist_form = AccountantForm()
    return render(request, 'register.html',
        context={'regist_form':regist_form})


def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
        
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        accountant = authenticate(username=username, password=password)

        if accountant:
            if accountant.is_active:
                login(request, accountant)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, 'Authentication Error')
        else:
            messages.error(request, "Wrong Username or Password")
    return render(request, 'login.html', {'form':AccountantForm()})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
