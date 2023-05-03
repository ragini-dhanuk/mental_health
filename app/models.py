from django.db import models

# Create your models here.
class Message(models.Model):
    client = models.CharField(max_length=50)
    psychiatrist = models.CharField(max_length=50)
    Message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.client
    
    # def __str__(self):
        # return self.psychiatrist

class Feedback(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()
      message = models.TextField()
      rating = models.IntegerField()

      def __str__(self):
        return self.name