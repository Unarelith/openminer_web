from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib.admin.views.decorators import staff_member_required

from .models import Mod
from .forms import ModForm

def view(request, id):
    mod = get_object_or_404(Mod, id=id)
    return render(request, 'contentdb/mod_view.html', locals())

def list(request):
    mods = Mod.objects.all()
    return render(request, 'contentdb/mod_list.html', locals())

@staff_member_required
def new(request):
    form = ModForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form_ok = True
        mod = form.save(commit=False)
        mod.user = request.user
        try:
            mod.save()
        except:
            form_ok = False

        return redirect(reverse('contentdb:mod_list')
                + (("?new=" + str(mod.id)) if form_ok == True else '?new=ko'), permanent=True)

    model_name = "mod"
    return render(request, 'contentdb/object_new.html', locals())

@staff_member_required
def edit(request, id):
    mod = get_object_or_404(Mod, id=id)
    form = ModForm(request.POST or None, request.FILES or None, instance=mod)
    if form.is_valid():
        form_ok = True
        newmod = form.save(commit=False)
        mod = newmod
        mod.user = request.user
        try:
            mod.save()
        except:
            form_ok = False
        return redirect(reverse('contentdb:mod_list')
                + (("?edit=" + str(mod.id)) if form_ok == True else '?edit=ko'), permanent=True)

    model_name = "mod"
    model_id = mod.id
    return render(request, 'contentdb/object_edit.html', locals())

@staff_member_required
def remove(request, id):
    mod = get_object_or_404(Mod, id=id)
    mod.delete()

    return redirect(reverse('contentdb:mod_list') + "?delete=ok", permanent=True)

