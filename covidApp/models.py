from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    father_name = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default="Male")
    district = models.CharField(max_length=50, null=True, blank=True)
    village = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    is_infected = models.BooleanField()
    travelled = models.BooleanField()
    travel_country = models.CharField(max_length=50, null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class TestingCenter(models.Model):
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    detail = models.TextField()

    def __str__(self):
        return self.name


class Helpline(models.Model):
    state = models.TextField(max_length=50)
    contact = models.BigIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.state


class Hospital(models.Model):
    name = models.TextField()
    doctor_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    contact = models.BigIntegerField()

    def __str__(self):
        return self.name
