from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from contentdb.models import EngineVersion, Mod, ModVersion, TexturePack, TexturePackVersion
from .serializers import EngineVersionSerializer, ModSerializer, ModVersionSerializer, TexturePackSerializer, TexturePackVersionSerializer

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

    def get_object(self):
        mod_id = self.kwargs.get('id')
        version_id = self.kwargs.get('version_id')

        mod = Mod.objects.get(id=mod_id)

        return ModVersion.objects.get(version_id=version_id, mod=mod)

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

    def get_object(self):
        id = self.kwargs.get('id')
        version_id = self.kwargs.get('version_id')

        texture_pack = TexturePack.objects.get(id=id)

        return ModVersion.objects.get(version_id=version_id, texture_pack=texture_pack)

