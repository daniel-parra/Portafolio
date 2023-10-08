from django.contrib import admin
from .models import Server

# Register your models here.
class ServerAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_actualizacion']

admin.site.register(Server, ServerAdmin)