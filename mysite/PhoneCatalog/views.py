from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  render
from .models import  PhoneCatalog
def index(request):
    tupl = PhoneCatalog.objects.all()
    info = {"phones":tupl}
    return  render(request,"index.html",info)

