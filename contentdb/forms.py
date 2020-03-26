from django import forms

from .models import Mod, TexturePack

class ModForm(forms.ModelForm):
    class Meta:
        model = Mod
        fields = ['name']

class TexturePackForm(forms.ModelForm):
    class Meta:
        model = TexturePack
        fields = ['name']

