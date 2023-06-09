from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tasks.models import Usuario
import re

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        nombres = request.POST['Nombres']
        apellidos = request.POST['Apellidos']
        departamento = request.POST.get('Departamento')
        municipio = request.POST.get('Municipio')
        direccion = request.POST['Dirección']
        tipo_doc = request.POST.get('Tipo_doc')
        n_doc = request.POST['N_doc']
        correo = request.POST['Correo']
        contraseña = request.POST['Contraseña']
        n_cel = request.POST['N_cel']

        # Crear una instancia de User
        user = User()

        # Asignar valores a los campos
        user.username = username
        user.set_password(contraseña)
        user.email = correo
        user.first_name = nombres
        user.last_name = apellidos

        # Guardar el usuario en la base de datos
        user.save()
        # Crear una instancia de Usuario y asociarla a la instancia de User
        usuario = Usuario.objects.create(user=user, departamento=departamento, municipio=municipio, direccion=direccion, tipo_doc=tipo_doc, n_doc=n_doc, n_cel=n_cel, fecha_creacion=date.today())

        return redirect('index')
    
    else:
        return render(request, 'registro.html')
    
def inicio_sesion(request):
    if request.method == 'POST':

        identificador = request.POST['identificador']
        contraseña = request.POST['Contraseña']

        if es_correo_electronico(identificador):
            print('Estas iniciando sesion con correo electronico')
            user = authenticate(email=identificador, password=contraseña)
            if user is not None:
                # Autenticación exitosa, inicia sesión
                login(request, user)
                print('inicio exitoso')
                # Redirige a la página deseada
                return redirect('inicio')
            else:
                # Autenticación fallida, muestra un mensaje de error o realiza alguna acción
                print('inicio fallido')
                return redirect('login')

        else:
            print('Estas iniciando sesion con username')
            user = authenticate(username=identificador, password=contraseña)
            if user is not None:
                # Autenticación exitosa, inicia sesión
                login(request, user)
                print('inicio exitoso')
                # Redirige a la página deseada
                return render(request, 'inicio.html', {'user': request.user})
            else:
                # Autenticación fallida, muestra un mensaje de error o realiza alguna acción
                print('inicio fallido')
                return redirect('login')
    
    else:
        return render(request, 'login.html')

def inicio(request):
    return render(request, 'inicio.html')

def salir(request):
    return render(request, 'index.html')


def es_correo_electronico(cadena):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(patron, cadena):
        return True
    else:
        return False
