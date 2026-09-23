from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
    ]

    titulo = models.CharField(max_length=200)
    curso = models.CharField(max_length=100)
    fecha_entrega = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='tareas')

    def __str__(self):
        return f"{self.titulo} - {self.estado}"