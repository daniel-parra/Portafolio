from django.db import models

# Create your models here.
class Server(models.Model):
    nombre = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    estado = models.BooleanField(default=True)
    decripcion = models.TextField(blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"
        ordering = ["-fecha_actualizacion"]

    def __str__(self) -> str:
        return self.title
    
class Ambient(models.Model):
    nombre = models.CharField(max_length=100)