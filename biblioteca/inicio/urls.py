from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("login", views.login_a, name="login"),
    path("logout", views.logout_a, name="logout"),
    path("index", views.index, name="index")
]
