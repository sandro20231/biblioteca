from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LivroViewSet



urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("login", views.login_a, name="login"),
    path("logout", views.logout_a, name="logout"),
    path("index", views.index, name="index"),
    path('novoautor', views.novoautor, name="novoautor"),
    path('listaautor', views.listaautor, name="listaautor"),
    path('listaautor/<int:id>', views.exibirautor, name="exibirautor"),
    path('buscarautoradeletar', views.buscarautoradeletar,
         name="buscarautoradeletar"),
    path('excluirautor', views.excluirautor, name="excluirautor"),
    path('busc', views.busc, name="busc"),
    path('alterarautor', views.alterarautor, name='alterarautor'),
    path('novolivro', views.novolivro, name="novolivro"),
    path('todoslivros', views.todoslivros, name="todoslivros"),
    path('buscadeletar', views.buscadeletar, name="buscadeletar"),
    path('deletarlivro', views.deletarlivro, name='deletarlivro'),
   
]
