from django.db import models
from django.contrib.auth.models import User
from clients.models import Client

# Create your models here.
class Psychiatrist(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    full_name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100)
    phone = models.IntegerField()
    addreess = models.TextField(max_length=100)
    details = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='psychiatrists/images/', blank=True, null=True)
    fees = models.IntegerField()
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
    
class Prescription(models.Model):
    subject = models.CharField(max_length=50)
    content = models.TextField()
    duration = models.DurationField()
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    psychiatrist =  models.ForeignKey(Psychiatrist, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.subject
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='psychiatrists/images/', blank=True, null=True)
    content = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=50)
    author = models.ForeignKey( Psychiatrist, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.title

    