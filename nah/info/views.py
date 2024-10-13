from django.shortcuts import render
from django.http import HttpResponse
from .models import info

# Create your views here.
def home(request):
    return render(request, 'home.html')

def list(request):
    Data = {'Infomation': info.objects.all().order_by('-id')}
    return render(request, 'info\info.html', Data)