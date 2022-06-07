from django import forms

        #FORMULARIOS PERSONAS

class AgregarPersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    # input_format hace que se pueda ingresar la fecha con el formato latino, dia/mes/año
    fecha_nacimiento = forms.DateField(label="fecha_nacimiento", input_formats=["%d/%m/%Y"],
    #widget es para poder agregar un tip para que el usuario sepa como ingresar la fecha
    widget=forms.TextInput(attrs={'placeholder': '30/12/1995'}))
    altura = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': "1.75 m"}))
    #nombre_mascota = forms.CharField(label="Nombre mascota", max_length=100)
    #tipo = forms.CharField(label="Tipo", max_length=100)
    #raza = forms.CharField(label="Raza", max_length=100)
    #nombre_alimento = forms.CharField(label="Nombre de alimento", max_length=100)
    #peso = forms.CharField(label="Peso", max_length=100)


class BuscarPersonaForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar_persona")

class ActualizarPersonaForm(AgregarPersonaForm):
    id = forms.IntegerField(widget = forms.HiddenInput())

         #FORMULARIOS MASCOTAS

class AgregarMascotaForm(forms.Form):
    nombre_mascota = forms.CharField(label="Nombre mascota", max_length=100)
    tipo = forms.CharField(label="Tipo", max_length=100)
    raza = forms.CharField(label="Raza", max_length=100)
    #nombre_alimento = forms.CharField(label="Nombre de alimento", max_length=100)
    #peso = forms.CharField(label="Peso", max_length=100)


class BuscarMascotaForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar_mascota")

class ActualizarMascotaForm(AgregarMascotaForm):
    id = forms.IntegerField(widget = forms.HiddenInput())