from django.urls import path
from rest_framework_swagger.views import get_swagger_view

from . import views

schema_view = get_swagger_view(title='OpenMiner content API')

urlpatterns = [
    # path('',                                       schema_view),

    path('news',                                   views.NewsArticleList.as_view()),
    path('news/<int:pk>',                          views.NewsArticleRetrieve.as_view()),

    path('version',                                views.EngineVersionList.as_view()),
    path('version/<int:pk>',                       views.EngineVersionRetrieve.as_view()),

    path('mod',                                    views.ModList.as_view()),
    path('mod/<int:pk>',                           views.ModRetrieve.as_view()),

    path('mod/version',                            views.ModVersionList.as_view()),
    path('mod/version/<int:pk>',                   views.ModVersionRetrieve.as_view()),

    path('texture_pack',                           views.TexturePackList.as_view()),
    path('texture_pack/<int:pk>',                  views.TexturePackRetrieve.as_view()),

    path('texture_pack/version/<int:pk>',          views.TexturePackList.as_view()),
    path('texture_pack/version/<int:pk>',          views.TexturePackRetrieve.as_view()),
]

