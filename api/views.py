from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from contentdb.models import EngineVersion, Mod, ModVersion, TexturePack, TexturePackVersion
from .serializers import EngineVersionSerializer, ModSerializer, ModVersionSerializer, TexturePackSerializer, TexturePackVersionSerializer

class EngineVersionListCreate(generics.ListCreateAPIView):
    serializer_class = EngineVersionSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return EngineVersion.objects.filter()

    def perform_create(self, serializer):
        serializer.save()

class EngineVersionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EngineVersionSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return EngineVersion.objects.filter()

class ModListCreate(generics.ListCreateAPIView):
    serializer_class = ModSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Mod.objects.filter()

    def perform_create(self, serializer):
        serializer.save()

class ModRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ModSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Mod.objects.filter()

class ModVersionListCreate(generics.ListCreateAPIView):
    serializer_class = ModVersionSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ModVersion.objects.filter()

    def perform_create(self, serializer):
        serializer.save()

class ModVersionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ModVersionSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return ModVersion.objects.filter()

class TexturePackListCreate(generics.ListCreateAPIView):
    serializer_class = TexturePackSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TexturePack.objects.filter()

    def perform_create(self, serializer):
        serializer.save()

class TexturePackRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TexturePackSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TexturePack.objects.filter()

class TexturePackVersionListCreate(generics.ListCreateAPIView):
    serializer_class = TexturePackVersionSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TexturePackVersion.objects.filter()

    def perform_create(self, serializer):
        serializer.save()

class TexturePackVersionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TexturePackVersionSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TexturePackVersion.objects.filter()

