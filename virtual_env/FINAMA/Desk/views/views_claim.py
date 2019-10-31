from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Data piutang
@login_required
def claim(request):
    return render(request, 'data_piutang/data_piutang.html')
