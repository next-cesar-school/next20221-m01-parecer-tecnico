from multiprocessing import AuthenticationError
from django.contrib import admin
from api.models import Cliente,Equipamento,ParecerDoTecnico

# Register your models here.

#admin.site.register(admin)
admin.site.register(Cliente)
admin.site.register(Equipamento)
admin.site.register(ParecerDoTecnico)

