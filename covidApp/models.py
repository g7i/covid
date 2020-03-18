from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    father_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
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
