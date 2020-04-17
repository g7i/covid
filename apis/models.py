from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Advisory(models.Model):
    lang = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    detail = models.TextField()
    is_update = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Advisories'


class Awareness(models.Model):
    lang = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='awareness/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Awarenesses"


class GovtData(models.Model):
    national = models.IntegerField(blank=True, null=True)
    international = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)
    cured = models.IntegerField(blank=True, null=True)
    cases = models.IntegerField(blank=True, null=True)
    is_state = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)


class Precaution(models.Model):
    lang = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    details = models.TextField()
    is_lockdown = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CoronaAudio(models.Model):
    audio = models.FileField(upload_to='audios/')
    user_id = models.IntegerField()
    isBefore = models.BooleanField()

    def __str__(self):
        return f'{self.user_id}'


class Requirement(models.Model):
    rashan = models.CharField(max_length=50, null=True, blank=True)
    gas = models.CharField(max_length=50, null=True, blank=True)
    medical = models.CharField(max_length=50, null=True, blank=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    emergency = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    colony = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    house = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField()

    def __str__(self):
        return f'{self.mobile}'


class Neighbour(models.Model):
    REL = (
        ('N', "Neighbour"),
        ('F', 'Friend'),
    )
    rel = models.CharField(max_length=50, choices=REL)
    name = models.CharField(max_length=50)
    colony = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, null=True, blank=True)
    house = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField()

    def __str__(self):
        return self.name


class DailyBasis(models.Model):
    state = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    ward = models.CharField(max_length=150)
    date = models.CharField(max_length=150)
    authority = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    post = models.CharField(max_length=150)
    food = models.CharField(max_length=150)
    vegetable = models.CharField(max_length=150)
    ration = models.CharField(max_length=150)
    farmer = models.CharField(max_length=150)
    milk = models.CharField(max_length=150)
    other = models.CharField(max_length=150)
    announcement = models.TextField()
    remarks = models.TextField()

    def __str__(self):
        return f'{self.state} {self.district} {self.ward}'


class Home(models.Model):
    name = models.CharField(max_length=100)
    aadhar = models.BigIntegerField()
    image = models.ImageField(upload_to='home/')
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    from_district = models.CharField(max_length=100)
    to_district = models.CharField(max_length=100)
    from_state = models.CharField(max_length=100)
    to_state = models.CharField(max_length=100)
    date_of_journey = models.DateField()
    reason = models.CharField(max_length=100)
    have_tested = models.BooleanField()
    have_infected = models.BooleanField()
    mobile_number = models.BigIntegerField()
    is_approved = models.BooleanField(default=False)
    approval_date = models.DateField(null=True)

    def __str__(self):
        return self.name
