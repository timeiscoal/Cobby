from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    phonenum = models.CharField(max_length=20, verbose_name='전화번호')
    email = models.EmailField(max_length=100, blank=False ,verbose_name='이메일')
