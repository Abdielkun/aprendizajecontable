from .models import Inscripcion

def informacion_usuario(request):
    if request.user.is_authenticated:
        # Busca suscripción activa (Pagada y de categoría 'Suscripcion')
        suscripcion = Inscripcion.objects.filter(
            usuario=request.user, 
            pagado=True, 
            curso__categoria='Suscripcion'
        ).first()
        return {'suscripcion_activa': suscripcion}
    return {}