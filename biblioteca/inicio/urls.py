from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("login", views.login_a, name="login"),
    path("logout", views.logout_a, name="logout"),
    path("index", views.index, name="index"),
    path('novoautor', views.novoautor, name="novoautor"),
    path('listaautor', views.listaautor, name="listaautor"),
    path('listaautor/<int:id>', views.exibirautor, name="exibirautor"),
    path('buscarautoradeletar', views.buscarautoradeletar, name="buscarautoradeletar"),
    path('excluirautor', views.excluirautor, name="excluirautor")
]
