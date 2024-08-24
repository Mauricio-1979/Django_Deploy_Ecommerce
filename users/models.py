from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
  AbstractBaseUser,
  PermissionsMixin,
  UserManager
)

class CustomUsersManager(UserManager):
  def _create_user(self, email, password, **extrafields):
    if not email:
      raise ValueError("You must enter an email")
    
    email = self.normalize_email(email)
    user = self.model(email= email, **extrafields)
    user.set_password(password)
    user.save(using=self._db)

    return user
  
  def create_user(self, email=None, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", False)
    return self._create_user(email, password, **extra_fields)
  
  def create_superuser(self, email=None, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault('is_superuser', True)
    return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
  email = models.CharField(max_length=100, unique=True)
  name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  avatar = models.ImageField(default="avatar.png")
  date_joined = models.DateTimeField(default=timezone.now)
  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)

  objects = CustomUsersManager()
  USERNAME_FIELD ="email"
  REQUIRED_FIELDS = []

  class Meta:
    ordering = ["-date_joined"]

  def __str__(self):
    return f"{self.name} - {self.avatar.url if self.avatar else 'No Avatar'}"
    #return self.name + " - " + self.avatar

