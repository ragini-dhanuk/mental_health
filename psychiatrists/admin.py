from django.contrib import admin

# Register your models here.
from .models import Psychiatrist,Prescription,Article
@admin.register(Psychiatrist)
class PsychiatristAdmin(admin.ModelAdmin):
  '''Admin View for Psychiatrist '''
  list_display = ('user','full_name','qualification','phone','addreess','details','city','photo','fees','create_on','update_on')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
  '''Admin View for Prescription '''
  list_display = ('psychiatrist','client','subject','content','duration','create_on','update_on')

admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
  '''Admin View for Article '''
  list_display = ('psychiatrist','title','image','content','create_on','update_on')
