from django import forms

<<<<<<< HEAD
from products.models import *
=======
from accounts.models import *
>>>>>>> 3988bb483a692b890a9972ae661314ce133bbb0b


class ProductListForm(forms.ModelForm):
    product_name = forms.CharField(widget=forms.HiddenInput())
    product_price = forms.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        model = Product


class ProductDetailForm(forms.ModelForm):
    product_id = forms.IntegerField()
    product_name = forms.CharField(max_length=40)
    product_info = forms.CharField(max_length=200)
    product_price = forms.DecimalField(decimal_places=2, max_digits=10)
    available = forms.CharField(max_length=20)