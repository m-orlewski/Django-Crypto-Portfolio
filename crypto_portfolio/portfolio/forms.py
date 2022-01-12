from django import forms
from django.forms.widgets import NumberInput

class AssetForm(forms.Form):
    amount = forms.FloatField(label="amount", widget=NumberInput(attrs={'class': 'inp'}))
    price = forms.FloatField(label="price", widget=NumberInput(attrs={'class': 'inp'}))
    date = forms.DateTimeField(label='date', widget=NumberInput(attrs={'type': 'date', 'class':'inp'}))
    id = forms.CharField(widget=forms.HiddenInput(), label='id')