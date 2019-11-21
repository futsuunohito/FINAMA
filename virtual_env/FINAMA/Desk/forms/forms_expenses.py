from django import forms
from django.contrib.auth.models import User
from Desk.models import Pengeluaran

class inputForm (forms.Form):
    deskripsi_pengeluaran   = forms.CharField(label = "Deskripsi", widget = forms.Textarea, help_text = "pengeluaran apa yang dikeluarkan?")
    biaya                   = forms.DecimalField(label = "Jumlah Pembelian",help_text = "Rp.69420")
    # nama_barang.render('nama_barang', 'Kacang Atom')
    