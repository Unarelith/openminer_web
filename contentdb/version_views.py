from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.contrib.admin.views.decorators import staff_member_required

from .models import EngineVersion
from .forms import EngineVersionForm

def view(request, id):
    version = get_object_or_404(EngineVersion, id=id)
    return render(request, 'contentdb/version_view.html', locals())

def list(request):
    versions = EngineVersion.objects.all()
    return render(request, 'contentdb/version_list.html', locals())

@staff_member_required
def new(request):
    form = EngineVersionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form_ok = True
        version = form.save(commit=False)
        version.user = request.user
        try:
            version.save()
        except:
            form_ok = False

        if form_ok:
            return redirect(reverse('contentdb:version_view', kwargs={"id": version.id}), permanent=True)
        else:
            return redirect(reverse('contentdb:version_list') + '?new=ko', permanent=True)

    model_name = "version"
    return render(request, 'object_new.html', locals())

@staff_member_required
def edit(request, id):
    version = get_object_or_404(EngineVersion, id=id)
    form = EngineVersionForm(request.POST or None, request.FILES or None, instance=version)
    if form.is_valid():
        form_ok = True
        newversion = form.save(commit=False)
        version = newversion
        version.user = request.user
        try:
            version.save()
        except:
            form_ok = False

        if form_ok:
            return redirect(reverse('contentdb:version_view', kwargs={"id": version.id}), permanent=True)
        else:
            return redirect(reverse('contentdb:version_list') + '?edit=ko', permanent=True)

    model_name = "version"
    model_id = version.id
    return render(request, 'object_edit.html', locals())

@staff_member_required
def remove(request, id):
    version = get_object_or_404(EngineVersion, id=id)
    version.delete()

    return redirect(reverse('contentdb:version_list') + "?delete=ok", permanent=True)


