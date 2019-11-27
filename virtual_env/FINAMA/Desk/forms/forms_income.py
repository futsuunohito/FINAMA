from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django_typeahead.widgets import TypeaheadInput
from Desk.models import Pendapatan

class inputForm (ModelForm):

    class Meta:
        model = Pendapatan
        fields = ('nama_barang', 'nama_pembeli', 'jumlah_pembelian', 'deskripsi_pendapatan')
        labels = {'nama_barang':"Nama Barang", 'nama_pembeli':'Nama Pembeli', 'jumlah_pembelian':'Jumlah Pembelian'}
        widgets = {
            'deskripsi_pendapatan'  : Textarea(attrs={'cols': 80, 'rows': 10}),
            'nama_barang'           : TypeaheadInput(
                options ={'hint': True, 'highlight': True, 'minLength': 1 },
                datasets={'name': 'barang', 'source': 'substringMatcher(barang)',}
            )
        }

        