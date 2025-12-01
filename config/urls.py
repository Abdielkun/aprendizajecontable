from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Públicas
    path('', views.home, name='home'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('capacitaciones/', views.capacitaciones, name='capacitaciones'),
    path('webinars/', views.webinars, name='webinars'),
    path('suscripciones/', views.suscripciones, name='suscripciones'),
    path('curso/<int:curso_id>/', views.detalle_curso, name='detalle_curso'),
    
    # Carrito
    path('carrito/', views.carrito, name='carrito'),
    path('carrito/add/<int:curso_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/del/<int:curso_id>/', views.eliminar_carrito, name='eliminar_carrito'),
    path('checkout/', views.checkout, name='checkout'),
    
    # Usuario
    path('mis-cursos/', views.mis_cursos, name='mis_cursos'),
    path('cancelar-suscripcion/<int:inscripcion_id>/', views.cancelar_suscripcion, name='cancelar_suscripcion'),
    
    # Auth
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro, name='registro'),
    path('salir/', views.salir, name='salir'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)