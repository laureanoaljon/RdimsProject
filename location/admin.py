from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Region, Province, City

# Register your models here.
# from import_export import resources
from .resources import RegionResource, ProvinceResource, CityResource

class RegionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RegionResource
    list_display = (
        'id',
        'psgcCode',
        'regDesc',
        'regCode',
        'population',
    )

    list_filter = (
        'regCode',
    )

class ProvinceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProvinceResource
    list_display = (
        'id',
        'psgcCode',
        'provDesc',
        'regCode',
        'provCode',
        'population',
    )

    list_filter = (
        'regCode',
    )

class CityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CityResource
    list_display = (
        'id',
        'psgcCode',
        'cityDesc',
        'regCode',
        'provId',
        'provCode',
        'cityCode',
        'population',
    )

    list_filter = (
        'regCode',
        'provId',
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "provId":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(CityAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


# Register for admin view
admin.site.register(Region, RegionAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(City, CityAdmin)