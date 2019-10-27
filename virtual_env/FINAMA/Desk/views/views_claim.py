from django.shortcuts import render

# Data piutang
def claim(request):
    return render(request, 'data_piutang/data_piutang.html')
