from django.contrib import admin
from .models import Helpline, Hospital, TestingCenter, Video, Faq, Member, User

from import_export.admin import ImportExportModelAdmin


@admin.register(Helpline)
class viewAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Hospital)
admin.site.register(User)
# admin.site.register(Helpline)
admin.site.register(Member)
admin.site.register(TestingCenter)
admin.site.register(Video)
admin.site.register(Faq)
