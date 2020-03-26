from django.contrib.auth.models import User

from rest_framework import serializers

from contentdb.models import EngineVersion, Mod, ModVersion, TexturePack, TexturePackVersion
from homepage.models import NewsArticle

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

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

