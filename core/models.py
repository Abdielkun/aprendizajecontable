from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    titulo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100, default="Contabilidad")
    precio_normal = models.DecimalField(max_digits=10, decimal_places=2)
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    imagen_url = models.URLField(max_length=500, null=True, blank=True)
    
    objetivo = models.TextField(default="Domina las normas contables...")
    temario = models.TextField(default="<ul><li>Módulo 1</li></ul>")
    
    destacado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def get_image(self):
        if self.imagen: return self.imagen.url
        return self.imagen_url if self.imagen_url else ''

class Inscripcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    pagado = models.BooleanField(default=False, verbose_name="¿Pago Validado?")

    def __str__(self):
        return f"{self.usuario.username} - {self.curso.titulo}"