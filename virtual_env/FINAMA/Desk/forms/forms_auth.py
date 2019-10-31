from django import forms
from django.contrib.auth.models import User
from Desk.models import Accountant

class AccountantForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

    def verify(self):
        verified = super(AccountantForm, self).clean()
        password = verified.get("password")
        confirm_password = verified.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password not match")
