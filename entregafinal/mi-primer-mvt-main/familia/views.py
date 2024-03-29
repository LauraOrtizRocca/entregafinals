from readline import append_history_file
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from familia.forms import *
from familia.models import Persona, Mascota, Alimento

        #DEFINO INDEX

def index(request):
    return render(request, "familia/index.html", {})

def index_2(request):
    personas = Persona.objects.all()
    mascotas = Mascota.objects.all()
    alimentos = Alimento.objects.all()

    context = {
        'personas': personas,
        'mascotas': mascotas,
        'alimentos': alimentos,
    }
    template = loader.get_template('familia/lista_familiares.html')
    return HttpResponse(render(request, 'familia/lista_familiares.html', context))

        #DEFINO PERSONAS Y SUS ACCIONES

def agregar_pesona(request):
    """Aquí se pueden agregar todos los campos"""

    if request.method == "POST":
        form = AgregarPersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            altura = form.cleaned_data['altura']
            #nombre_mascota = form.cleaned_data['nombre_mascota']
            #tipo = form.cleaned_data['tipo']
            #raza = form.cleaned_data['raza']
            #nombre_alimento = form.cleaned_data['nombre_alimento']
            #peso = form.cleaned_data['peso']

            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura).save()
           # Mascota(nombre_mascota=nombre_mascota, tipo= tipo, raza=raza).save()
           # Alimento(nombre_alimento=nombre_alimento, peso=peso).save()
            return HttpResponseRedirect(reverse("index_2"))

    elif request.method == "GET":
        form = AgregarPersonaForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")
    return render(request, 'familia/form_carga.html', {'form': form})


def borrar_persona(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar_persona(request, identificador):
    if request.method == "GET":
        persona = get_object_or_404(Persona, pk=int(identificador))
        initial = {
            "id": persona.id,
            "nombre": persona.nombre, 
            "apellido": persona.apellido, 
            "email": persona.email,
            "fecha_nacimiento": persona.fecha_nacimiento.strftime("%d/%m/%Y"),
            "altura": persona.altura,
  #          "nombre_mascota": persona.nombre_mascota,
  #          "tipo": persona.tipo,
  #          "raza": persona.raza,
  #          "nombre_alimento": persona.nombre_alimento,
  #          "peso": persona.peso
        }
    
        form_actualizar = ActualizarPersonaForm(initial=initial)
        return render(request, 'familia/form_carga.html', {'form': form_actualizar, 'actualizar': True})

    elif request.method == "POST":
        form_actualizar = ActualizarPersonaForm(request.POST)
        if form_actualizar.is_valid():
            persona = get_object_or_404(Persona, pk=form_actualizar.cleaned_data['id'])
            persona.nombre = form_actualizar.cleaned_data['nombre']
            persona.apellido = form_actualizar.cleaned_data['apellido']
            persona.email = form_actualizar.cleaned_data['email']
            persona.fecha_nacimiento = form_actualizar.cleaned_data['fecha_nacimiento']
            persona.altura = form_actualizar.cleaned_data['altura']
   #         persona.nombre_mascota = form_actualizar.cleaned_data['nombre_mascota']
   #         persona.tipo = form_actualizar.cleaned_data['tipo']
   #         persona.raza = form_actualizar.cleaned_data['raza']
   #         persona.nombre_alimento = form_actualizar.cleaned_data['nombre_alimento']
   #         persona.peso = form_actualizar.cleaned_data['peso']
            persona.save()

            return HttpResponseRedirect(reverse("index"))



def buscar_persona(request):
    if request.method == "GET":
        form_busqueda = BuscarPersonaForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPersonaForm(request.POST)
        personas = None
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            personas = Persona.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'familia/lista_familiares.html', {"personas": personas})
    
        
    
        # DEFINO MASCOTA Y SUS ACCIONES

def agregar_mascota(request):
    """Aquí se pueden agregar todos los campos"""

    if request.method == "POST":
        form = AgregarMascotaForm(request.POST)
        if form.is_valid():

            
            nombre_mascota = form.cleaned_data['nombre_mascota']
            tipo = form.cleaned_data['tipo']
            raza = form.cleaned_data['raza']
            #nombre_alimento = form.cleaned_data['nombre_alimento']
            #peso = form.cleaned_data['peso']

            Mascota(nombre_mascota=nombre_mascota, tipo= tipo, raza=raza).save()
           # Alimento(nombre_alimento=nombre_alimento, peso=peso).save()
            return HttpResponseRedirect(reverse("index_2"))

    elif request.method == "GET":
        form = AgregarMascotaForm()
    else:
        return HttpResponseBadRequest("Error no conozco ese metodo para esta request")
    return render(request, 'familia/form_carga_mascota.html', {'form': form})


def borrar_mascota(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        mascota = Mascota.objects.filter(id=int(identificador)).first()
        if mascota:
            mascota.delete()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar_mascota(request, identificador):
    if request.method == "GET":
        mascota = get_object_or_404(Mascota, pk=int(identificador))
        initial = {
            "id": mascota.id,
            "nombre_mascota": mascota.nombre_mascota,
            "tipo": mascota.tipo,
            "raza": mascota.raza,
  #          "nombre_alimento": persona.nombre_alimento,
  #          "peso": persona.peso
        }
    
        form_actualizar = ActualizarMascotaForm(initial=initial)
        return render(request, 'familia/form_carga_mascota.html', {'form': form_actualizar, 'actualizar': True})

    elif request.method == "POST":
        form_actualizar = ActualizarMascotaForm(request.POST)
        if form_actualizar.is_valid():
            mascota = get_object_or_404(Mascota, pk=form_actualizar.cleaned_data['id'])
            mascota.nombre_mascota = form_actualizar.cleaned_data['nombre_mascota']
            mascota.tipo = form_actualizar.cleaned_data['tipo']
            mascota.raza = form_actualizar.cleaned_data['raza']
   #         persona.nombre_alimento = form_actualizar.cleaned_data['nombre_alimento']
   #         persona.peso = form_actualizar.cleaned_data['peso']
            mascota.save()

            return HttpResponseRedirect(reverse("index"))



def buscar_mascota(request):
    if request.method == "GET":
        form_busqueda = BuscarMascotaForm()
        return render(request, 'familia/form_busqueda_mascota.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarMascotaForm(request.POST)
        mascotas = None
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            mascotas = Mascota.objects.filter(nombre_mascota__icontains=palabra_a_buscar)

        return  render(request, 'familia/lista_mascotas.html', {"mascotas": mascotas})
