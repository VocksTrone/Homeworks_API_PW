from rest_framework import serializers
from .models import Estudiante, Tarea

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id', 'nombre', 'email']


class TareaSerializer(serializers.ModelSerializer):
    # Formatea la fecha de entrega a YYYY-MM-DD
    fechaEntrega = serializers.DateField(source='fecha_entrega')

    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'curso', 'fechaEntrega', 'estado', 'estudiante']

    def validate_estado(self, value):
        if value not in ['pendiente', 'completada']:
            raise serializers.ValidationError("El estado debe ser 'pendiente' o 'completada'.")
        return value