from django.forms import ModelForm, Textarea, DateInput
from django.contrib.auth.models import User
from Desk.models import Piutang


class inputForm (ModelForm):

    class Meta:
        model = Piutang
        fields = ('asal_piutang', 'jumlah_piutang', 'jatuh_tempo', 'deskripsi_piutang')
        labels = {'asal_piutang' : 'Asal Piutang', 'deskripsi_piutang':'Deskripsi Piutang',
                 'jumlah_piutang':'Jumlah Piutang', 'jatuh_tempo':'Jatuh Tempo'}
        help_texts = {
            'asal_piutang'      : 'Pt. Suka Hutang',
            'jumlah_piutang'    : 45000, 
        }
        widgets = {
            'deskripsi_piutang' : Textarea(attrs={'cols': 80, 'rows': 10}),
            'jatuh_tempo'       : DateInput(attrs={
                'class': 'form-control datepicker-input', 'data-target':'#datepicker'
                }),
        }