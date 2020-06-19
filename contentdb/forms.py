from django import forms

from .models import EngineVersion, Mod, TexturePack

class EngineVersionForm(forms.ModelForm):
    class Meta:
        model = EngineVersion
        fields = ['name']

class ModForm(forms.ModelForm):
    class Meta:
        model = Mod
        fields = ['name']

class TexturePackForm(forms.ModelForm):
    class Meta:
        model = TexturePack
        fields = ['name']

