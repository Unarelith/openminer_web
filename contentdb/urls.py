from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import mod_views, texture_pack_views

app_name = "contentdb"

urlpatterns = [
    path('mod/<int:id>', mod_views.view, name='mod_view'),
    path('mod/list',     mod_views.list, name='mod_list'),

    path('texture_pack/<int:id>', texture_pack_views.view, name='texture_pack_view'),
    path('texture_pack/list',     texture_pack_views.list, name='texture_pack_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

