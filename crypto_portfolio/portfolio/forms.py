from django import forms

class AssetForm(forms.Form):
    amount = forms.FloatField(label="amount")
    price = forms.FloatField(label="price")
    id = forms.CharField(widget=forms.HiddenInput(), label='id')
        