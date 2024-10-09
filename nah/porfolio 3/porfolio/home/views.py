from django.shortcuts import render
from django.http import HttpResponse
from .models import Infor
# Create your views here.

def home(request):
    data = {
        'Infor': Infor.objects.all(),
    }
    return render(request, 'home.html',data)