from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=150, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 

    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'users_customuser'