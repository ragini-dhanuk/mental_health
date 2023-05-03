from django.db import models

# Create your models here.
class UserTypeChoice(models.TextChoices):
    CLIENT = 'C', 'client'
    PSYCHIATRIST = 'P',  'psychiatrist'
class Profile(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    user_type = models.CharField(max_length=2, choices=UserTypeChoice.choices, default=UserTypeChoice.CLIENT)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)

    def _str_(self):
        return self.name