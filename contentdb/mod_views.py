from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Mod

def view(request, id):
    mod = get_object_or_404(Mod, id=id)
    return render(request, 'contentdb/mod_view.html', locals())

def list(request):
    mods = Mod.objects.all()
    return render(request, 'contentdb/mod_list.html', locals())

