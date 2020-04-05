from django.contrib import admin
from import_export import resources
from import_export.resources import ModelResource
from import_export.results import RowResult

from .models import Helpline, Hospital, TestingCenter, Video, Faq, Member, User

from import_export.admin import ImportMixin


class TestingCenterResource(resources.ModelResource):

    def import_row(self, row, instance_loader, **kwargs):
        import_result = super(ModelResource, self).import_row(
            row, instance_loader, **kwargs
        )
        if row['name'] is None:
            import_result.import_type = RowResult.IMPORT_TYPE_SKIP
        return import_result

    class Meta:
        skip_unchanged = True
        report_skipped = True
        raise_errors = False
        model = TestingCenter


@admin.register(TestingCenter)
class TestingCenterAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = TestingCenterResource


class HelplineResource(resources.ModelResource):

    def import_row(self, row, instance_loader, **kwargs):
        import_result = super(ModelResource, self).import_row(
            row, instance_loader, **kwargs
        )
        if row['state'] is None:
            import_result.import_type = RowResult.IMPORT_TYPE_SKIP
        return import_result

    class Meta:
        skip_unchanged = True
        report_skipped = True
        raise_errors = False
        model = Helpline


@admin.register(Helpline)
class HelplineAdmin(ImportMixin, admin.ModelAdmin):
    resource_class = HelplineResource


admin.site.register(Hospital)
admin.site.register(User)
# admin.site.register(Helpline)
admin.site.register(Member)
# admin.site.register(TestingCenter)
admin.site.register(Video)
admin.site.register(Faq)
