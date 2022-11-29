from django import forms
from django.forms import ModelForm, TextInput
from .models import Catalogue


class CatalogueForm(ModelForm):
    class Meta:
        model = Catalogue
        fields = '__all__'
