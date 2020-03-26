from django.contrib import admin
from .models import Helpline, Hospital, TestingCenter, Video, Faq, Member

admin.site.register(Hospital)
admin.site.register(Helpline)
admin.site.register(Member)
admin.site.register(TestingCenter)
admin.site.register(Video)
admin.site.register(Faq)