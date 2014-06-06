from django import forms
from accounts.models import *

class ProfileDetailForm(forms.ModelForm):
    address = forms.ModelMultipleChoiceField(queryset=Address.objects.all())
    cart = forms.InlineForeignKeyField(widget=forms.HiddenInput())

    class Meta:
        model = User

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30)
    phone = forms.CharField()
    address = forms.ModelMultipleChoiceField(queryset=Address.objects.all())

    class Meta:
        model = User

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=30)
    phone = forms.CharField()
    address = forms.ModelMultipleChoiceField(queryset=Address.objects.all())

    class Meta:
        model = User