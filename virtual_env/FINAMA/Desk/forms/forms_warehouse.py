from django.forms import ModelForm, Textarea, HiddenInput
from django.contrib.auth.models import User
from Desk.models import Barang

class inputForm (ModelForm):
    
    class Meta:
        model = Barang
        fields = ('nama_barang', 'distributor', 'jumlah_barang',
                 'satuan', 'harga_beli', 'harga_jual', 'deskripsi_barang',)
        labels = {
            'nama_barang'       :"Nama Barang", 
            'distributor'       :'Nama Distributor', 
            'deskripsi_barang'  :'Deskripsi Barang',
            'jumlah_barang'     :'Jumlah Barang',
            'harga_beli'        :'Harga Beli', 
            'harga_jual'        :'Harga Jual', 
            }
        help_texts = {
            'nama_barang'       :"Dead Meat", 
            'distributor'       :'NecroCorp', 
            'deskripsi_barang'  :'What did you expect',
            'jumlah_barang'     :'666',
            'satuan'            :'kg',
            'harga_beli'        :'69000', 
            'harga_jual'        :'99000', 
            }
        widgets = {
            'deskripsi_barang'  : Textarea(attrs={'cols': 80, 'rows': 10}),
        }