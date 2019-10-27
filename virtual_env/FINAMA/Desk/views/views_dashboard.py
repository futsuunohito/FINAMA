from django.shortcuts import render

# Dashboard with graphics
def index(request):
    return render(request, 'main.html')
