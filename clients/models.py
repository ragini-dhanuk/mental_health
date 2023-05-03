from site import USER_BASE
from django.db import models

# Create your models here.
class Client(models.Model):
  user = models.CharField(max_length=50)
  full_name = models.CharField(max_length=100)
  age = models.IntegerField() 
  gender = models.CharField(max_length=10)
  city = models.TextField(max_length=50)
  phone = models.IntegerField()
  photo = models.ImageField(upload_to='clients/images/', blank=True, null=True)
  created_on = models.DateTimeField(auto_now_add=True)
  update_on = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.full_name
  


