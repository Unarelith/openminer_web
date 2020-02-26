from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='OpenMiner content API')

urlpatterns = [
    path('',                      schema_view),

    path('mod',                   views.ModListCreate.as_view()),
    path('mod/<int:pk>',          views.ModRetrieveUpdateDestroy.as_view()),

    path('texture_pack',          views.TexturePackListCreate.as_view()),
    path('texture_pack/<int:pk>', views.TexturePackRetrieveUpdateDestroy.as_view()),
]

