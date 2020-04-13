from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class User(AbstractUser):
    father_name = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default="Male")
    district = models.CharField(max_length=50, null=True, blank=True)
    village = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    is_infected = models.BooleanField(default=False)
    symptoms = models.BooleanField(default=False)
    cured = models.BooleanField(default=False)
    travelled = models.BooleanField(default=False)
    mobile = models.IntegerField(null=True, blank=True)
    pin = models.IntegerField(null=True, blank=True)
    travel_country = models.CharField(max_length=50, null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class Member(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=7, choices=GENDER)
    aadhar = models.BigIntegerField()
    is_infected = models.BooleanField(default=False)
    decl_date = models.DateField(null=True, blank=True)
    isolated = models.BooleanField(default=False)
    idk = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    symptoms = models.BooleanField(default=False)
    cured = models.BooleanField(default=False)
    travelled = models.BooleanField(default=False)
    death = models.BooleanField(default=False)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    from_date = models.DateField(null=True, blank=True)
    pin = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)

    def __str__(self):
        return str(self.aadhar)


class TestingCenter(models.Model):
    CAT = (
        ('TC', 'TC'),
        ('SC', 'SC'),
        ('PR', "PR"),
    )
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=50)
    is_operational = models.BooleanField(default=True)
    detail = models.TextField()
    cat = models.CharField(max_length=2, choices=CAT)

    def __str__(self):
        return self.name


class Helpline(models.Model):
    state = models.TextField(max_length=50)
    contact1 = models.BigIntegerField()
    contact2 = models.BigIntegerField(blank=True, null=True)
    contact3 = models.BigIntegerField(blank=True, null=True)
    contact4 = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField()
    lang = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.state


class Hospital(models.Model):
    name = models.TextField()
    doctor_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    contact = models.BigIntegerField()
    state = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=150, null=True)
    level = models.CharField(max_length=150, null=True)
    email = models.EmailField(null=True)

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

    def __str__(self):
        return self.que[:30]
