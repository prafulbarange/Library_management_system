from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

# CustomUser Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=13, default=False)
    password = models.CharField(max_length=100)
     
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
# Book Create Model    
class BookDetails(models.Model):
    bookname = models.CharField(max_length=150)
    authors= models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    entry_time_date = models.DateTimeField(auto_now_add=True)