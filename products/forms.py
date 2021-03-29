from django import forms
from django.forms import fields, widgets

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'heheBoi', 'placeholder': 'Enter you title'}
            ),
        }


# for django pure forms
class RawProductForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'heheBoi', 'placeholder': 'Enter your title'}
        )
    )
