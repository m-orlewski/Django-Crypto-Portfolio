from django import forms
from django.forms.widgets import NumberInput

class AssetForm(forms.Form):
    amount = forms.FloatField(label="amount")
    price = forms.FloatField(label="price")
    date = forms.DateTimeField(label='date', widget=NumberInput(attrs={'type': 'date'}))
    id = forms.CharField(widget=forms.HiddenInput(), label='id')
        