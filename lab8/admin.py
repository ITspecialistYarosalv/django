from django.contrib import admin
from .models import Client, Phone, Call, Tariff

admin.site.register(Client)
admin.site.register(Phone)
admin.site.register(Call)
admin.site.register(Tariff)

