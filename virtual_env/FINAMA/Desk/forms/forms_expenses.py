from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from Desk.models import Pengeluaran

class inputForm (ModelForm):
    
    class Meta:
        model = Pengeluaran
        fields = ('biaya', 'deskripsi_pengeluaran', )
        labels = {'deskripsi_pengeluaran':"Deskripsi Pengeluaran",}
        help_texts = {
            'biaya' : 45000
        }
        widgets = {
            'deskripsi_pengeluaran'  : Textarea(attrs={'cols': 80, 'rows': 10}),
        }