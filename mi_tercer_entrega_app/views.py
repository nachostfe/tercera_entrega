from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


from .models import Familiar, Curso, Estudiante,Disco, Auto,Banda,Recital

from .forms import CursoForm, EstudianteForm,DiscoForm, AutoForm,BandasForm,RecitalesForm

from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse


def inicio(request):
    return render(request, 'mi_tercer_entrega_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola, mundo!")


def saludo_con_template(request):
    return render(request, 'mi_tercer_entrega_app/saludo.html')


def crear_familiar(request, nombre):
    if nombre is not None:
        # Creamos un nuevo objeto Familiar
        nuevo_familiar = Familiar(
            nombre=nombre,
            apellido="ApellidoEjemplo",
            edad=30,
            fecha_nacimiento="1993-01-01",
            parentesco="Primo"
        )
        nuevo_familiar.save()
    return render(request, "mi_tercer_entrega_app/crear_familiar.html", {"nombre": nombre})

@login_required
def crear_curso(request):

    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                activo=form.cleaned_data['activo']
            )
            nuevo_curso.save()
            return redirect('cursos')
    else:
        form = CursoForm()
        return render(request, 'mi_tercer_entrega_app/crear_curso.html', {'form': form})
    
    
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_tercer_entrega_app/cursos.html', {'cursos': cursos})


def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_tercer_entrega_app/cursos.html', {'cursos': cursos, 'nombre': nombre})


def crear_estudiante(request):

    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
                fecha_inscripcion=form.cleaned_data['fecha_inscripcion']
            )
            nuevo_curso.save()
            return redirect('inicio')
    else:
        form = EstudianteForm()
        return render(request, 'mi_tercer_entrega_app/crear_estudiante.html', {'form': form})


class AutoListView(ListView):
    model = Auto
    template_name = 'mi_tercer_entrega_app/listar_autos.html'
    context_object_name = 'autos'


class AutoCreateView(CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'mi_tercer_entrega_app/crear_auto.html'
    success_url = reverse_lazy('listar-autos')


class AutoDetailView(DetailView):
    model = Auto
    template_name = 'mi_tercer_entrega_app/detalle_auto.html'
    context_object_name = 'auto'


class AutoUpdateView(UpdateView):
    model = Auto
    form_class = AutoForm
    template_name = 'mi_tercer_entrega_app/crear_auto.html'
    success_url = reverse_lazy('listar-autos')


class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'mi_tercer_entrega_app/eliminar_auto.html'
    success_url = reverse_lazy('listar-autos')

class RecitalesCreateView(CreateView):
    model = Recital
    form_class = RecitalesForm
    template_name = 'mi_tercer_entrega_app/crear-recitales.html'
    success_url = reverse_lazy('listar-recitales')
 
 
 
@login_required
def crear_disco(request):
    if request.method == 'POST':
        form = DiscoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_disco = Disco(
                banda=form.cleaned_data['banda'],
                titulo=form.cleaned_data['titulo'],
                genero=form.cleaned_data['genero'],
                anio=form.cleaned_data['anio'],
                precio=form.cleaned_data['precio']
            )
            nuevo_disco.save()
            return redirect('inicio')
    else:
        form = DiscoForm()
        return render(request, 'mi_tercer_entrega_app/crear_disco.html', {'form': form})

def lista_discos(request):
    discos = Disco.objects.all()
    return render(request, 'mi_tercer_entrega_app/lista_discos.html', {'discos': discos})

@login_required
def buscar_discos(request):
    if request.method == 'GET':
        titulo = request.GET.get('titulo', '')
        discos = Disco.objects.filter(titulo__icontains=titulo)
        return render(request, 'mi_tercer_entrega_app/lista_discos.html', {'discos': discos, 'titulo': titulo})
 
 
 
 
class BandasCreateView(CreateView):
    model = Banda
    form_class = BandasForm
    template_name = 'mi_tercer_entrega_app/crear-bandas.html'
    success_url = reverse_lazy('listar-bandas')
    
class BandasUpdateView(UpdateView):
    model = Banda
    form_class = BandasForm
    template_name = 'mi_tercer_entrega_app/crear-bandas.html'
    success_url = reverse_lazy('listar-bandas')
    
class BandasDeleteView(DeleteView):
    model = Banda
    template_name = 'mi_tercer_entrega_app/eliminar-banda.html'
    success_url = reverse_lazy('listar-bandas')
    
class BandasListView(ListView):
    model = Banda
    template_name = 'mi_tercer_entrega_app/listar-bandas.html'
    context_object_name = 'bandas'
    
class BandasDetailView(DetailView):
    model = Banda
    template_name = 'mi_tercer_entrega_app/detalle_banda.html'
    context_object_name = 'bandas'

def acercade(request):
    return render(request, 'mi_tercer_entrega_app/acercade.html')