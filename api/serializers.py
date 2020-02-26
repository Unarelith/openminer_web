from rest_framework import serializers

from contentdb.models import Mod, TexturePack

class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mod
        fields = '__all__'

class TexturePackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TexturePack
        fields = '__all__'

