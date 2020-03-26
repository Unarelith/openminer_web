from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib.admin.views.decorators import staff_member_required

from .models import TexturePack
from .forms import TexturePackForm

def view(request, id):
    texture_pack = get_object_or_404(TexturePack, id=id)
    return render(request, 'contentdb/texture_pack_view.html', locals())

def list(request):
    texture_packs = TexturePack.objects.all()
    return render(request, 'contentdb/texture_pack_list.html', locals())

@staff_member_required
def new(request):
    form = TexturePackForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form_ok = True
        texture_pack = form.save(commit=False)
        texture_pack.user = request.user
        try:
            texture_pack.save()
        except:
            form_ok = False

        if form_ok:
            return redirect(reverse('contentdb:texture_pack_view', kwargs={"id": texture_pack.id}), permanent=True)
        else:
            return redirect(reverse('contentdb:texture_pack_list') + '?new=ko', permanent=True)

    model_name = "texture_pack"
    return render(request, 'object_new.html', locals())

@staff_member_required
def edit(request, id):
    texture_pack = get_object_or_404(TexturePack, id=id)
    form = TexturePackForm(request.POST or None, request.FILES or None, instance=texture_pack)
    if form.is_valid():
        form_ok = True
        new_texture_pack = form.save(commit=False)
        texture_pack = new_texture_pack
        texture_pack.user = request.user
        try:
            texture_pack.save()
        except:
            form_ok = False

        if form_ok:
            return redirect(reverse('contentdb:texture_pack_view', kwargs={"id": texture_pack.id}), permanent=True)
        else:
            return redirect(reverse('contentdb:texture_pack_list') + '?edit=ko', permanent=True)

    model_name = "texture_pack"
    model_id = texture_pack.id
    return render(request, 'object_edit.html', locals())

@staff_member_required
def remove(request, id):
    texture_pack = get_object_or_404(TexturePack, id=id)
    texture_pack.delete()

    return redirect(reverse('contentdb:texture_pack_list') + "?delete=ok", permanent=True)


