from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "homepage"

login_view = auth_views.LoginView.as_view(template_name="login_form.html")
logout_view = auth_views.LogoutView.as_view()

urlpatterns = [
    path('',       views.home,  name='home'),
    path('login',  login_view,  name='login'),
    path('logout', logout_view, name='logout'),
]

