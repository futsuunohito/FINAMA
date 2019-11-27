from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Desk.models import Pendapatan, Pengeluaran, Piutang
from django.db.models import Sum

# Dashboard with graphics
@login_required
def index(request):
    try:
        income = Pendapatan.objects.aggregate(Sum('total_pendapatan'))['total_pendapatan__sum']
    except:
        income = 0
    try:
        expense = Pengeluaran.objects.aggregate(Sum('biaya'))['biaya__sum']
    except:
        expense = 0
    try:
        claim = Piutang.objects.aggregate(Sum('jumlah_piutang'))['jumlah_piutang__sum']
    except:
        claim = 0
    profit = income - expense
    context = {
        "income"  : income,
        "expense" : expense,
        "claim"   : claim,
        "profit"  : profit,
    }
    return render(request, 'main.html', context)
