from django.contrib import admin
from import_export import resources
from import_export.resources import ModelResource
from import_export.results import RowResult

from .models import (
    Advisory,
    Awareness,
    GovtData,
    Precaution,
    CoronaAudio,
    Neighbour,
    Requirement,
    DailyBasis,
    Home,
    Bank,
)
from import_export.admin import ImportMixin


class GovtDataResource(resources.ModelResource):

    def import_row(self, row, instance_loader, **kwargs):
        import_result = super(ModelResource, self).import_row(
            row, instance_loader, **kwargs
        )
        if row['latitude'] is None and row['longitude'] is None:
            import_result.import_type = RowResult.IMPORT_TYPE_SKIP
        return import_result

    class Meta:
        skip_unchanged = True
        report_skipped = True
        raise_errors = False
        model = GovtData


@admin.register(GovtData)
class GovtDataAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = GovtDataResource


admin.site.register(Advisory)
admin.site.register(Awareness)
admin.site.register(Precaution)
admin.site.register(CoronaAudio)
admin.site.register(Neighbour)
admin.site.register(DailyBasis)
admin.site.register(Requirement)
admin.site.register(Home)
admin.site.register(Bank)
