
from django.urls import path

from .views import (saludo, saludo_con_template, crear_familiar, inicio, crear_curso, crear_estudiante, 
                    buscar_cursos,lista_discos,acercade,buscar_discos, cursos, crear_disco,RecitalesCreateView,
                    BandasCreateView,BandasDetailView,BandasDeleteView,BandasUpdateView,BandasListView,
                    AutoCreateView, AutoListView, AutoDeleteView, AutoDetailView, AutoUpdateView)
urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crear_familiar),
    path('crear-curso/', crear_curso, name='crear-curso'),
    path('crear-estudiante/', crear_estudiante, name='crear-estudiante'),
    path('cursos/', cursos, name='cursos'),
    path('cursos/buscar', buscar_cursos, name='buscar-cursos'),
    path('disco/', crear_disco, name='disco'),
    
     # urls con vistas basadas en clase
    path('listar-autos/', AutoListView.as_view(), name='listar-autos'),
    path('crear-auto/', AutoCreateView.as_view(), name='crear-auto'),
    #path('editar/<int:pk>/', AutoUpdateView.as_view(), name='editar-auto'),
    path('eliminar/<int:pk>/', AutoDeleteView.as_view(), name='eliminar-auto'),
    path('detalle-auto/<int:pk>', AutoDetailView.as_view(), name='detalle-auto'),
    
    
    path('discos/', lista_discos, name='lista_discos'),
    path('discos/buscar/', buscar_discos, name='buscar_discos'),
    path('acerca-de/', acercade, name='acercade'),
    path('crear-recitales/', RecitalesCreateView.as_view(), name='crear-recitales'),
    
    path('crear-bandas/', BandasCreateView.as_view(), name='crear-bandas'),
    path('detalle-banda/<int:pk>', BandasDetailView.as_view(), name='detalle-banda'),
    path('eliminar-banda/<int:pk>/', BandasDeleteView.as_view(), name='eliminar-banda'),
    path('editar/<int:pk>/', BandasUpdateView.as_view(), name='editar-banda'),
    path('listar-bandas/', BandasListView.as_view(), name='listar-bandas'),
]
