from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='OpenMiner content API')

urlpatterns = [
    path('',                                               schema_view),

    path('mod',                                            views.ModList.as_view()),
    path('mod/<int:pk>',                                   views.ModRetrieve.as_view()),

    path('mod/<int:id>/version',                           views.ModVersionList.as_view()),
    path('mod/<int:id>/version/<int:version_id>',          views.ModVersionRetrieve.as_view()),

    path('texture_pack',                                   views.TexturePackList.as_view()),
    path('texture_pack/<int:pk>',                          views.TexturePackRetrieve.as_view()),

    path('texture_pack/<int:id>/version/<int:version_id>', views.TexturePackList.as_view()),
    path('texture_pack/<int:id>/version/<int:version_id>', views.TexturePackRetrieve.as_view()),
]

