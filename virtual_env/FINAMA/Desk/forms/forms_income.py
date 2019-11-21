from django import forms
from django.contrib.auth.models import User
from Desk.models import Pendapatan

class inputForm (forms.Form):
    nama_barang         = forms.CharField(label = "Nama Barang", help_text = "Kecap Guriz")
    nama_pembeli        = forms.CharField(label = "Nama Pembeli", help_text = "Bambang Pabambang")
    jumlah_pembelian    = forms.DecimalField(label = "Jumlah Pembelian",help_text = 69420)
    deskripsi           = forms.CharField(widget = forms.Textarea, help_text = "Such a weird order he got there")
    # nama_barang.render('nama_barang', 'Kacang Atom')
    


# class incomeInput (forms.ModelForm):
#     # nama_barang = "Kacang C4 PT Atomic Laboratory"
#     # nama_pembeli = "Alan Pejalan"
#     # jumlah_pembelian = 420
#     # deskripsi = "Bomb has been planted"
#     class Meta:
#         model = Pendapatan
#         fields = ('nama_barang', 'nama_pembeli', 'jumlah_pembelian', 'deskripsi')
#         labels = {'nama_barang':"Nama Barang", 'nama_pembeli':'Nama Pembeli', 'jumlah_pembelian':'Jumlah Pembelian'}
#         help_texts = {
#             'nama_barang':"Kecap Gurih", 
#             'nama_pembeli':"Bambang Pabambang", 
#             'jumlah_pembelian':69420, 
#             'deskripsi': "Such a weird order he got there",}
