from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from contentdb.models import Mod, TexturePack
from .serializers import ModSerializer, TexturePackSerializer

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
