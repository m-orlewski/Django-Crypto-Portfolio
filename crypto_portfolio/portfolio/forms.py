from django import forms

class AssetForm(forms.Form):
    amount = forms.FloatField(label="amount")
    id = forms.CharField(widget=forms.HiddenInput(), label='id')
        