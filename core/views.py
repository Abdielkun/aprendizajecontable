from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from .models import Curso, Inscripcion
from .forms import RegistroUsuarioForm

def home(request):
    cursos = Curso.objects.filter(destacado=True)[:3]
    if not cursos: cursos = Curso.objects.all().order_by('-id')[:3]
    return render(request, 'core/home.html', {'cursos': cursos})

def nosotros(request):
    return render(request, 'core/nosotros.html')

def capacitaciones(request):
    query = request.GET.get('q')
    cat = request.GET.get('cat')
    cursos = Curso.objects.all().order_by('-id')
    
    if query: cursos = cursos.filter(Q(titulo__icontains=query))
    if cat: cursos = cursos.filter(categoria=cat)
        
    return render(request, 'core/capacitaciones.html', {'cursos': cursos})

def webinars(request):
    return render(request, 'core/webinars.html')

def suscripciones(request):
    mensual = Curso.objects.filter(titulo="Suscripción Mensual").first()
    semestral = Curso.objects.filter(titulo="Suscripción Semestral").first()
    anual = Curso.objects.filter(titulo="Suscripción Anual").first()
    return render(request, 'core/suscripciones.html', {'mensual': mensual, 'semestral': semestral, 'anual': anual})

def detalle_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    inscrito = False
    if request.user.is_authenticated:
        inscrito = Inscripcion.objects.filter(usuario=request.user, curso=curso).exists()
    return render(request, 'core/detalle_curso.html', {'curso': curso, 'inscrito': inscrito})

# Carrito
def carrito(request):
    ids = request.session.get('carrito', [])
    cursos = Curso.objects.filter(id__in=ids)
    total = sum(c.precio_oferta for c in cursos)
    return render(request, 'core/carrito.html', {'cursos': cursos, 'total': total})

def agregar_carrito(request, curso_id):
    if 'carrito' not in request.session: request.session['carrito'] = []
    carrito = request.session['carrito']
    if curso_id not in carrito:
        carrito.append(curso_id)
        request.session.modified = True
    return redirect('carrito')

def eliminar_carrito(request, curso_id):
    carrito = request.session.get('carrito', [])
    if curso_id in carrito:
        carrito.remove(curso_id)
        request.session.modified = True
    return redirect('carrito')

@login_required(login_url='login')
def checkout(request):
    ids = request.session.get('carrito', [])
    if not ids: return redirect('capacitaciones')
    cursos = Curso.objects.filter(id__in=ids)
    total = sum(c.precio_oferta for c in cursos)
    
    if request.method == 'POST':
        for curso in cursos:
            if not Inscripcion.objects.filter(usuario=request.user, curso=curso).exists():
                Inscripcion.objects.create(usuario=request.user, curso=curso, pagado=False)
        request.session['carrito'] = []
        return render(request, 'core/gracias.html')
    return render(request, 'core/checkout.html', {'cursos': cursos, 'total': total})

# Panel Usuario
@login_required(login_url='login')
def mis_cursos(request):
    # Suscripción
    mi_suscripcion = Inscripcion.objects.filter(usuario=request.user, pagado=True, curso__categoria='Suscripcion').first()
    # Cursos individuales
    cursos_activos = Inscripcion.objects.filter(usuario=request.user, pagado=True).exclude(curso__categoria='Suscripcion')
    # Pendientes
    cursos_pendientes = Inscripcion.objects.filter(usuario=request.user, pagado=False)
    
    return render(request, 'core/mis_cursos.html', {
        'mi_suscripcion': mi_suscripcion,
        'cursos_activos': cursos_activos,
        'cursos_pendientes': cursos_pendientes
    })

@login_required
def cancelar_suscripcion(request, inscripcion_id):
    suscripcion = get_object_or_404(Inscripcion, id=inscripcion_id, usuario=request.user)
    if request.method == 'POST':
        suscripcion.delete()
    return redirect('mis_cursos')

# Auth
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    return render(request, 'core/login.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'core/registro.html', {'form': form})

def salir(request):
    logout(request)
    return redirect('home')