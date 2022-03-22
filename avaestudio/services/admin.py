from django.contrib import admin
from .models import Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

#Registramos servicio y su configuracion
admin.site.register(Service, ServiceAdmin)