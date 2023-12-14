from django.shortcuts import render, HttpResponse

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