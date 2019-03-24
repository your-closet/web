from django import forms
from .models import *


class ClothingTypeForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = ['clothing_type']


class ClothingForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = [
            'brand', 'color', 'pattern', 'size', 'is_advertisable',
            'clothing_type'
        ]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
