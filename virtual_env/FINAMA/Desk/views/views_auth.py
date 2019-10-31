from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def user_register(request):
    return render(request, 'register.html')

def user_login(request):
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
