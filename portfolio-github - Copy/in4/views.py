from django.shortcuts import render
from django.http import HttpResponse
from .models import info

# Create your views here.

def list(request):
    Data = {'Infomation': info.objects.all().order_by('-id')}
    return render(request, 'in4.html', Data)