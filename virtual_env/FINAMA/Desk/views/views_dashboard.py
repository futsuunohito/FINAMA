from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Dashboard with graphics
@login_required
def index(request):
    return render(request, 'main.html')
