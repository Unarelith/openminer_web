from rest_framework import serializers

from contentdb.models import EngineVersion, Mod, ModVersion, TexturePack, TexturePackVersion

class EngineVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineVersion
        fields = '__all__'

class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mod
        fields = '__all__'

class ModVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModVersion
        fields = '__all__'

class TexturePackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TexturePack
        fields = '__all__'

class TexturePackVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TexturePackVersion
        fields = '__all__'

