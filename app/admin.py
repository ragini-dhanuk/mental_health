from django.contrib import admin
from .models import Message
from .models import Feedback
# Register your models here.

# @admin.register(Message)
# class MessageAdmin(admin.ModelAdmin):
  # '''Admin View for Message'''
  # list_display = ('client','psychiatrist','message')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    '''Admin View for Feedback'''
    list_display = ('name', 'email', 'rating', 'message')
    
