from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from contentdb.models import EngineVersion, Mod, ModVersion, TexturePack, TexturePackVersion
from homepage.models import NewsArticle

from .serializers import EngineVersionSerializer, ModSerializer, ModVersionSerializer, TexturePackSerializer, TexturePackVersionSerializer, NewsArticleSerializer, UserSerializer

class EngineVersionList(generics.ListAPIView):
    queryset = EngineVersion.objects.all()
    serializer_class = EngineVersionSerializer

class EngineVersionRetrieve(generics.RetrieveAPIView):
    queryset = EngineVersion.objects.all()
    serializer_class = EngineVersionSerializer

class ModList(generics.ListAPIView):
    queryset = Mod.objects.all()
    serializer_class = ModSerializer

class ModRetrieve(generics.RetrieveAPIView):
    queryset = Mod.objects.all()
    serializer_class = ModSerializer

class ModVersionList(generics.ListAPIView):
    queryset = ModVersion.objects.all()
    serializer_class = ModVersionSerializer

class ModVersionRetrieve(generics.RetrieveAPIView):
    queryset = ModVersion.objects.all()
    serializer_class = ModVersionSerializer

class TexturePackList(generics.ListAPIView):
    queryset = TexturePack.objects.all()
    serializer_class = TexturePackSerializer

class TexturePackRetrieve(generics.RetrieveAPIView):
    queryset = TexturePack.objects.all()
    serializer_class = TexturePackSerializer

class TexturePackVersionList(generics.ListAPIView):
    queryset = TexturePackVersion.objects.all()
    serializer_class = TexturePackVersionSerializer

class TexturePackVersionRetrieve(generics.RetrieveAPIView):
    queryset = TexturePackVersion.objects.all()
    serializer_class = TexturePackVersionSerializer

class NewsArticleList(generics.ListAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

class NewsArticleRetrieve(generics.RetrieveAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieve(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

