from django.contrib import admin
from django.utils.html import format_html
from .models import Curso, Inscripcion

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio_oferta', 'categoria', 'ver_imagen')
    list_filter = ('categoria',)
    def ver_imagen(self, obj):
        return format_html('<img src="{}" width="50" />', obj.get_image()) if obj.get_image() else "-"

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso', 'fecha', 'estado', 'aprobar')
    list_filter = ('pagado',)
    actions = ['aprobar_masivo']

    def fecha(self, obj): return obj.fecha_inscripcion.strftime("%d/%m/%Y %H:%M")
    
    def estado(self, obj):
        if obj.pagado: return format_html('<span style="background:green;color:white;padding:2px 6px;border-radius:4px">PAGADO</span>')
        return format_html('<span style="background:red;color:white;padding:2px 6px;border-radius:4px">PENDIENTE</span>')
    
    def aprobar(self, obj):
        if not obj.pagado:
            return format_html('<a class="button" style="background:#28a745;" href="/admin/core/inscripcion/{}/change/">Aprobar</a>', obj.id)
        return "-"

    def aprobar_masivo(self, request, queryset):
        queryset.update(pagado=True)
    aprobar_masivo.short_description = "Aprobar Pagos Seleccionados"