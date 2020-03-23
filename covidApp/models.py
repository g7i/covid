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
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    is_infected = models.BooleanField(default=False)
    travelled = models.BooleanField(default=False)
    family_infected = models.IntegerField(default=0)
    mobile = models.IntegerField(null=True, blank=True)
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


class Video(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField()
    lang = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title


class Faq(models.Model):
    TYPE = (
        ("WM", "WM"),
        ("RM", "RM"),
    )

    que = models.TextField()
    ans = models.TextField()
    lang = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE)
