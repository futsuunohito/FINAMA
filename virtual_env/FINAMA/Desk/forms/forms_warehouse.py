from django.forms import ModelForm, Textarea, HiddenInput
from django.contrib.auth.models import User
from Desk.models import Barang

class inputForm (ModelForm):
    # nama_barang = forms.CharField(label="Nama Barang", help_text="Gelas Glass")
    # distributor = forms.CharField(help_text="PT. Distribusi Normal")
    # deskripsi_barang = forms.CharField(widget=forms.Textarea, 
    #     label="Deskripsi Barang", help_text="Barang pecah belah bos")

    # jumlah_barang = forms.DecimalField(label="Jumlah Barang", help_text=432)
    # satuan = forms.DecimalField(label="Harga Satuan", help_text="Rp666000")
    # harga_beli = forms.DecimalField(label="Harga Beli", help_text="Rp600000")
    # harga_jual = forms.DecimalField(label="Harga Jual", help_text="Rp700000")
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