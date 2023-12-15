from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from core.models import Adoptantes

# Create your views here.

def landing(request):
    return render(request, "index.html")

def anicata(request):
    return render(request, "aniCata.html")

def anidet(request):
    return render(request, "aniDet.html")

def aniform(request):
    return render(request, "aniForm.html")

def pgaccess(request):
    return render(request, "pgAcces.html")

def pgini(request):
    return render(request, "PgIni.html")

def regform(request):
    return render(request, "regForm.html")

def register(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        password = request.POST['password']
        name = request.POST['name']
        lastName = request.POST['lastName']
        DNI = request.POST['DNI']
        email = request.POST['email']

        if Adoptantes.objects.filter(email=email).exists():
            messages.error(request, 'Ya existe un usuario con este correo electrónico.')
        else:
            user_profile = Adoptantes(userName=userName, password=password, name=name, lastName=lastName, DNI=DNI, email=email)
            user_profile.save()
            messages.success(request, 'Usuario creado exitosamente.')

            return redirect('regform')

    return render(request, 'regform.html')

def lista_adoptantes(request):
    adoptantes = Adoptantes.objects.all()
    return render(request, 'adopt.html')