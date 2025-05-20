from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
