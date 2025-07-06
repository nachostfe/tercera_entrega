from django.contrib import admin

# Register your models here.
from .models import Familiar, Curso, Estudiante, Disco

register_models = [Familiar, Curso, Estudiante,Disco]

admin.site.register(register_models)