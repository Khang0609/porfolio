from django.contrib import admin
from .models import info
from django.shortcuts import render

class infoAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'birthday', 'gender', 'phone', 'email', 'address']
    list_filter = ['name','age']
    search_fields = ['name']

# Register your models here.
admin.site.register(info, infoAdmin)
