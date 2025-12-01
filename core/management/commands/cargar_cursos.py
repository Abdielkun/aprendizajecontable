from django.core.management.base import BaseCommand
from core.models import Curso

class Command(BaseCommand):
    help = 'Carga los cursos iniciales del proyecto'

    def handle(self, *args, **kwargs):
        datos = [
            {
                "titulo": "CONTABILIDAD Y TRIBUTACIÓN EN EL SECTOR TEXTIL",
                "precio_normal": 200.00, "precio_oferta": 140.00, "categoria": "Tributaria",
                "imagen_url": "https://centrodecapacitacion.acaprendizajecontable.com/storage/training/contabilidad-y-tributacion-en-el-sector-textil.jpeg"
            },
            {
                "titulo": "MATEMÁTICA FINANCIERA DESDE CERO",
                "precio_normal": 180.00, "precio_oferta": 130.00, "categoria": "Finanzas",
                "imagen_url": "https://centrodecapacitacion.acaprendizajecontable.com/storage/training/matematica-financiera-desde-cero.jpeg"
            },
            {
                "titulo": "ELABORACIÓN DE CONTRATOS TRIBUTARIOS SUNAT",
                "precio_normal": 150.00, "precio_oferta": 120.00, "categoria": "Legal",
                "imagen_url": "https://centrodecapacitacion.acaprendizajecontable.com/storage/training/elaboracion-de-contratos-tributarios-sunat.jpeg"
            },
            {
                "titulo": "COSTOS Y PRESUPUESTOS 2025 EN EXCEL",
                "precio_normal": 250.00, "precio_oferta": 200.00, "categoria": "Excel",
                "imagen_url": "https://centrodecapacitacion.acaprendizajecontable.com/storage/training/costos-y-presupuestos-2025-en-excel.jpeg"
            },
            {
                "titulo": "ANALISTA CONTABLE Y TRIBUTARIO 2025",
                "precio_normal": 220.00, "precio_oferta": 150.00, "categoria": "Contabilidad",
                "imagen_url": "https://centrodecapacitacion.acaprendizajecontable.com/storage/training/analista-contable-y-tributario-2025.jpeg"
            },
             {
                "titulo": "AUDITORÍA FINANCIERA DESDE CERO",
                "precio_normal": 180.00, "precio_oferta": 110.00, "categoria": "Auditoría",
                "imagen_url": "https://centrodecapacitacion.acaprendizajecontable.com/storage/training/elaboracion-practica-de-una-auditoria-financiera-desde-cero-con-papeles-de-trabajo.jpeg"
            }
        ]

        for item in datos:
            Curso.objects.get_or_create(
                titulo=item['titulo'],
                defaults=item
            )
        
        self.stdout.write(self.style.SUCCESS('¡Cursos cargados exitosamente con las imágenes originales!'))
        