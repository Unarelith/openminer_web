from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import TexturePack

def view(request, id):
    texture_pack = get_object_or_404(TexturePack, id=id)
    return render(request, 'contentdb/texture_pack_view.html', locals())

def list(request):
    texture_packs = TexturePack.objects.all()
    return render(request, 'contentdb/texture_pack_list.html', locals())

