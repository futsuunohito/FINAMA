from django import forms
from django.contrib.auth.models import User
from Desk.models import Piutang


class inputForm (forms.Form):
    asal_piutang = forms.CharField(label = "Asal", help_text="PT. Suka Ngutang")
    deskripsi_piutang = forms.CharField(widget=forms.Textarea, label="Deskripsi", 
                                        help_text="Katanya buat modal jualan cilor")
    jumlah_piutang = forms.DecimalField(label="Jumlah Piutang", help_text="Rp112.358.132,1")
    jatuh_tempo = forms.DateTimeField(widget=forms.SelectDateWidget, label="Jatuh Tempo")