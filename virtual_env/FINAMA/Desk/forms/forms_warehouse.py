from django import forms
from django.contrib.auth.models import User
from Desk.models import Barang

class inputForm (forms.Form):
    nama_barang = forms.CharField(label="Nama Barang", help_text="Gelas Glass")
    distributor = forms.CharField(help_text="PT. Distribusi Normal")
    deskripsi_barang = forms.CharField(widget=forms.Textarea, 
        label="Deskripsi Barang", help_text="Barang pecah belah bos")

    jumlah_barang = forms.DecimalField(label="Jumlah Barang", help_text=432)
    satuan = forms.DecimalField(label="Harga Satuan", help_text="Rp666000")
    harga_beli = forms.DecimalField(label="Harga Beli", help_text="Rp600000")
    harga_jual = forms.DecimalField(label="Harga Jual", help_text="Rp700000")