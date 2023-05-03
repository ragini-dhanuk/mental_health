from django.contrib import admin

# Register your models here.
from .models import Client

admin.site.register(Client)

list_display = ('user','full_name','age','gender','city','phone','photo','created_on')



