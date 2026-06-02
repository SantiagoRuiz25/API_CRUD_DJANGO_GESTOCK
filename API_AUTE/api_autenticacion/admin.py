from django.contrib import admin
from .models import Roles, Usuarios, ContrasenaHash, RecuperacionContrasena

admin.site.register(Roles)
admin.site.register(Usuarios)
admin.site.register(ContrasenaHash)
admin.site.register(RecuperacionContrasena)



