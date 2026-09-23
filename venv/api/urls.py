from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudianteViewSet, TareaViewSet

router = DefaultRouter()
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]