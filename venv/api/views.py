from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Estudiante, Tarea
from .serializers import EstudianteSerializer, TareaSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    def get_queryset(self):
        queryset = Tarea.objects.all()
        estado = self.request.query_params.get('estado', None)
        
        if estado is not None:
            if estado not in ['pendiente', 'completada']:
                return Tarea.objects.none()
            queryset = queryset.filter(estado=estado)
            
        return queryset

    def partial_update(self, request, *args, **kwargs):
        estado = request.data.get('estado')
        if estado and estado not in ['pendiente', 'completada']:
            return Response(
                {"error": "Valor de estado inválido"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().partial_update(request, *args, **kwargs)