from django.contrib import admin

# Register your models here.
from .models import Familiar, Curso, Estudiante, Disco, Banda, Recital

register_models = [Familiar, Curso, Estudiante,Disco, Banda, Recital]

admin.site.register(register_models)