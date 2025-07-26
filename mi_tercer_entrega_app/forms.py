from django import forms
from .models import Auto,Recital,Banda

class CursoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    duracion_semanas = forms.IntegerField(min_value=1, initial=4)
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    activo = forms.BooleanField(required=False, initial=True)


class EstudianteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField()
    edad = forms.IntegerField(min_value=10, max_value=100)
    fecha_inscripcion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

class DiscoForm(forms.Form):
    banda = forms.CharField(label="Banda", max_length=100)
    titulo = forms.CharField(label="Titulo", max_length=100)
    genero = forms.CharField(label="Genero", max_length=100)
    fechaLanzamiento = forms.DateField(label="Fecha de Lanzamiento", 
        widget=forms.DateInput(attrs={'type': 'date'}))
    precio = forms.FloatField()

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['modelo', 'marca', 'descripcion']
        
class BandasForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nombre','aniodeformacion','pais','genero','historia','genero']
        
class RecitalesForm(forms.ModelForm):
    class Meta:
        model = Recital
        fields = ['banda','lugar','fecha','ciudad','precio']