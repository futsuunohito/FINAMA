from django import forms
from django.contrib.auth.models import User
from Desk.models import Pendapatan

class inputForm (forms.ModelForm):

    class Meta:
        model = Pendapatan
        fields = ('nama_barang', 'nama_pembeli', 'jumlah_pembelian', 'deskripsi_pendapatan')
        labels = {'nama_barang':"Nama Barang", 'nama_pembeli':'Nama Pembeli', 'jumlah_pembelian':'Jumlah Pembelian'}
        help_texts = {
            'nama_pembeli':"Bambang Pabambang", 
            'jumlah_pembelian':69420, 
            'deskripsi_pendapatan': "Such a weird order he got there",}
