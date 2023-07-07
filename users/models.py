from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length= 100, blank=True, null=True)
    email = models.CharField(max_length=150, blank=True, unique=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password']
    USERNAME_FIELD = 'email'