from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('freelancer', 'Freelancer')
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    email = models.EmailField(unique=True)

    def __str__(self):
        return super.username
    
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return super.name 
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True,null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    availability = models.BooleanField(default=True)

def __str__(self):
    return f"{self.user.username}'s Profile"