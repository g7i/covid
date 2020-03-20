from django.contrib import admin
from .models import Helpline, Hospital, TestingCenter

admin.site.register(Hospital)
admin.site.register(Helpline)
admin.site.register(TestingCenter)