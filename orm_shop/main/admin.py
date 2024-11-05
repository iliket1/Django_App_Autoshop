from django.contrib import admin
from .models import Car, Sale, Client

# зарегистрируйте необходимые модели
admin.site.register(Car)
admin.site.register(Sale)
admin.site.register(Client)
