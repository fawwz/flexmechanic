from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import GEOSGeometry
# from geopy.geocoders import Nominatim
# Create your models here.


# class Teacher(models.Model):
#     name = models.CharField(max_length=80)
#     age = models.IntegerField()

# class Teacher(models.Model):
#     name = models.CharField(max_length=80)
#     age = models.IntegerField()

class AccountType(models.TextChoices):
  MECHANIC = 'mechanic'
  CUSTOMER = 'customer'

class CustomUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('Please insert email')
    email = self.normalize_email(email)
    user = self.model(
        email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')

    return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True)
  email_validated = models.BooleanField(default=False)
  first_name = models.CharField(max_length=30, blank=True)
  last_name = models.CharField(max_length=30, blank=True)
  account_type = models.CharField(
      max_length=10, choices=AccountType.choices, default=AccountType.CUSTOMER)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_verified = models.BooleanField(default=False)

  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager() 



class Mechanic(gis_models.Model):
  user_profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  user_id = models.AutoField(primary_key=True)
  mechanic_name = models.CharField(max_length=100,null=True,blank=True)
  phone_number = models.CharField(max_length=15,null=True,blank=True)
  mechanic_nik = models.CharField(max_length=15,null=True,blank=True)
  # location_name = models.CharField(max_length=100, blank=True)
  # location_coordinates = gis_models.PointField(blank=True, null=True)
  # photo = models.ImageField(upload_to='image/', blank=True)
  
  # def save(self, *args, **kwargs):
  #   self.user_id = self.user.id
  #   geolocator = Nominatim(user_agent="")
  #   location = geolocator.geocode(self.location_name)
  #   point = GEOSGeometry(
  #       f"POINT({location.longitude} {location.latitude})", srid=4326)
  #   self.location_coordinates = point
  #   super().save(*args, **kwargs)

  def __str__(self):
    return self.user_profile.email

class Customer(gis_models.Model):
  user_profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  user_id = models.AutoField(primary_key=True)
  phone_number = models.CharField(max_length=15,default='08xxxxxxxxxx')
  location_coordinates = gis_models.PointField(blank=True, null=True)

  def __str__(self):
    return self.user_profile.email