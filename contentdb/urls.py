from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from . import version_views, mod_views, texture_pack_views

app_name = "contentdb"

urlpatterns = [
    path('version/<int:id>',              version_views.view,         name='version_view'),
    path('version/list',                  version_views.list,         name='version_list'),
    path('version/new',                   version_views.new,          name='version_new'),
    path('version/edit/<int:id>',         version_views.edit,         name='version_edit'),
    path('version/remove/<int:id>',       version_views.remove,       name='version_remove'),

    path('mod/<int:id>',                  mod_views.view,             name='mod_view'),
    path('mod/list',                      mod_views.list,             name='mod_list'),
    path('mod/new',                       mod_views.new,              name='mod_new'),
    path('mod/edit/<int:id>',             mod_views.edit,             name='mod_edit'),
    path('mod/remove/<int:id>',           mod_views.remove,           name='mod_remove'),

    path('texture_pack/<int:id>',         texture_pack_views.view,    name='texture_pack_view'),
    path('texture_pack/list',             texture_pack_views.list,    name='texture_pack_list'),
    path('texture_pack/new',              texture_pack_views.new,     name='texture_pack_new'),
    path('texture_pack/edit/<int:id>',    texture_pack_views.edit,    name='texture_pack_edit'),
    path('texture_pack/remove/<int:id>',  texture_pack_views.remove,  name='texture_pack_remove'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

