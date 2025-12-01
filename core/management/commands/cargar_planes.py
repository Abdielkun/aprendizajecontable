from django.core.management.base import BaseCommand
from core.models import Curso

class Command(BaseCommand):
    help = 'Carga los planes de suscripción como productos'

    def handle(self, *args, **kwargs):
        planes = [
            {
                "titulo": "Suscripción Mensual",
                "precio_normal": 250.00, 
                "precio_oferta": 190.00, 
                "categoria": "Suscripcion",
                "objetivo": "Acceso total por 30 días a todos los cursos en vivo y grabados.",
                "imagen_url": "https://centrodecapacitacion.acaprendizajecontable.com/images/LOGO_MENU.png"
            },
            {
                "titulo": "Suscripción Semestral",
                "precio_normal": 1200.00, 
                "precio_oferta": 1090.00, 
                "categoria": "Suscripcion",
                "objetivo": "Acceso total por 6 meses. Incluye certificación digital.",
                "imagen_url": "https://centrodecapacitacion.acaprendizajecontable.com/images/LOGO_MENU.png"
            },
            {
                "titulo": "Suscripción Anual",
                "precio_normal": 2400.00, 
                "precio_oferta": 2000.00, 
                "categoria": "Suscripcion",
                "objetivo": "Plan VIP por 1 año. Acceso a todo, asesoría y certificados físicos.",
                "destacado": True,
                "imagen_url": "https://centrodecapacitacion.acaprendizajecontable.com/images/LOGO_MENU.png"
            }
        ]

        for item in planes:
            Curso.objects.get_or_create(
                titulo=item['titulo'],
                defaults=item
            )
        
        self.stdout.write(self.style.SUCCESS('¡Planes de suscripción creados correctamente!'))