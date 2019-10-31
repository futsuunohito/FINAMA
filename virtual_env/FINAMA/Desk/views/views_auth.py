from django.shortcuts import render
from Desk.forms.forms_auth import AccountantForm
from Desk.views.views_dashboard import index

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == "POST":
        regist_form = AccountantForm(request.POST)

        if regist_form.is_valid():
            registrate = regist_form.save()
            registrate.set_password(registrate.password)
            registrate.save()

            return user_login(request)
        else:
            return HttpResponse("Registration Form Invalid")

    else:
        regist_form = AccountantForm()
        return render(request, 'register.html',
            context={'regist_form':regist_form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        accountant = authenticate(username=username, password=password)

        if accountant:
            if accountant.is_active:
                login(request, accountant)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Authentication Error')
        else:
            return HttpResponse('Wrong username or password')
    else:
        return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
