from django.contrib import admin

from .models import (
    Advisory,
    Awareness,
    GovtData,
    Precaution,
    CoronaAudio,
)

admin.site.register(Advisory)
admin.site.register(Awareness)
admin.site.register(GovtData)
admin.site.register(Precaution)
admin.site.register(CoronaAudio)
