from django import forms

from models import ProductOrder


class BuyShirtForm(forms.Form):
    size = forms.ChoiceField(choices=ProductOrder.SIZES, label="Choose your Size")