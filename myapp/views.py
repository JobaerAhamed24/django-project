from django.shortcuts import render
from .models import Service,About,Socile
# Create your views here.

def home(request):
    socile = Socile.objects.all()
    return render(request,'index.html',{'socile': socile})

def contact(request):
    return render(request,'contact.html')

def about(request):
    about = About.objects.all()
    return render(request,'about.html',{'about': about})
def resume(request):
    return render(request,'resume.html')
def service(request):
    service = Service.objects.all()
    return render(request,'service.html',{'service':service})