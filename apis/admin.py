from django.contrib import admin

from .models import (
    Advisory,
    Awareness,
    GovtData,
    Precaution,
    CoronaAudio,
    Neighbour,
    Requirement,
)
from import_export.admin import ImportExportModelAdmin


@admin.register(GovtData)
class viewAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Advisory)
admin.site.register(Awareness)
# admin.site.register(GovtData)
admin.site.register(Precaution)
admin.site.register(CoronaAudio)
admin.site.register(Neighbour)
admin.site.register(Requirement)
