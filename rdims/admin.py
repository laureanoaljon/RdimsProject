from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from location.models import Province, City
from .models import ProductionSupport, ExtensionService, MachineryEquipment, FacilityInfrastructure, FinancialAssistance, AewProfile, TrainingsAttended, TrainingsConducted, ProvinceCoordinate, CityCoordinate, RecognitionsAwardsReceived, CityMunicipalityProfile

# from ids.models import Ecosystem, Location, Months

# Register your models here.
# from import_export import resources
from .resources import ProductionSupportResource, ExtensionServiceResource, MachineryEquipmentResource, FacilityInfrastructureResource, FinancialAssistanceResource, AewProfileResource, TrainingsAttendedResource, TrainingsConductedResource, ProvinceCoordinateResource, CityCoordinateResource, RecognitionsAwardsReceivedResource, CityMunicipalityProfileResource

class ProductionSupportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProductionSupportResource
    list_display = (
        'id',
        'province',
        'municipality',
        'yearDate',
        'activityTitle',
        'leadImplementer',
        'agencyName',
        'category',
        'subCategory',
        'monthdayDate',
        'noOfUnits',
        'weightPerBag',
        'fertType',
        'noOfRecipient'
    )

    list_filter = (
        'province',
        'yearDate',
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(ProductionSupportAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "region":
    #         kwargs["queryset"] = Location.objects.filter(locType=1)
    #         return super().formfield_for_foreignkey(db_field, request, **kwargs)
    #     elif db_field.name == "province":
    #         kwargs["queryset"] = Location.objects.filter(locType=2)
    #         return super().formfield_for_foreignkey(db_field, request, **kwargs)
    #     elif db_field.name == "city":
    #         kwargs["queryset"] = Location.objects.filter(locType=3)
    #         return super().formfield_for_foreignkey(db_field, request, **kwargs)

class ExtensionServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ExtensionServiceResource
    list_display = (
        'id',
        'province',
        'municipality',
        'yearDate',
        'activityTitle',
        'leadImplementer',
        'agencyName',
        'category',
        'subCategory',
        'topics',
        'monthdayDate',
        'duration',
        'noOfFarmersServed'
    )

    list_filter = (
        'province',
        'yearDate',
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(ExtensionServiceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

class MachineryEquipmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MachineryEquipmentResource
    list_display = (
        'id',
        'province',
        'municipality',
        'yearDate',
        'activityTitle',
        'leadImplementer',
        'agencyName',
        'machEquipType',
        'monthdayDate',
        'noOfUnits',
        'fcaName'
    )

    list_filter = (
        'province',
        'yearDate',
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(MachineryEquipmentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

class FacilityInfrastructureAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FacilityInfrastructureResource
    list_display = (
        'id',
        'province',
        'municipality',
        'yearDate',
        'projectTitle',
        'fundSource',
        'amount',
        'category',
        'monthdayDate',
        'faciInfraType'
    )

    list_filter = (
        'province',
        'yearDate',
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(FacilityInfrastructureAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

class FinancialAssistanceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = FinancialAssistanceResource
    list_display = (
        'id',
        'province',
        'municipality',
        'yearDate',
        'activityTitle',
        'leadImplementer',
        'agencyName',
        'category',
        'monthdayDate',
        'totalAmount',
        'noOfFarmersAvailed'
    )

    list_filter = (
        'province',
        'yearDate',
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(FinancialAssistanceAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

class AewProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AewProfileResource
    list_display = (
        'id',
        'province',
        'municipality',
        'name',
        'position',
        'sex',
        'age',
        'employmentStatus',
        'yearsInService',
        'birthdate',
        'trainingsWanted',
        'remarks'
    )

    list_filter = (
        'province',
        'position'
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(AewProfileAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

class TrainingsAttendedAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TrainingsAttendedResource
    list_display = (
        'id',
        'province',
        'municipality',
        'date',
        'yearDate',
        'activityTitle',
        'topics',
        'trainingImplementer'
    )

    list_filter = (
        'province',
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(TrainingsAttendedAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

class TrainingsConductedAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TrainingsConductedResource
    list_display = (
        'id',
        'province',
        'municipality',
        'date',
        'yearDate',
        'activityTitle',
        'topics'
    )

    list_filter = (
        'province',
        'yearDate'
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(TrainingsConductedAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

class ProvinceCoordinateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ProvinceCoordinateResource
    list_display = (
        'id',
        'province',
        'coordinates'
    )

    list_filter = (
        'province',
    )

    # Alphabetical Province name
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "province":
    #         kwargs["queryset"] = Province.objects.all().order_by('provDesc')
    #     return super(TrainingsConductedAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class CityCoordinateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CityCoordinateResource
    list_display = (
        'id',
        'province',
        'municipality',
        'coordinates'
    )

    list_filter = (
        'province',
        'municipality'
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(CityCoordinateAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

class RecognitionsAwardsReceivedAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RecognitionsAwardsReceivedResource
    list_display = (
        'id',
        'province',
        'municipality',
        'dateAwarded',
        'titleOfAward',
        'awardingBody',
        'category',
        'awardeeName'
    )

    list_filter = (
        'province',
        'municipality',
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(RecognitionsAwardsReceivedAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

class CityMunicipalityProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CityMunicipalityProfileResource
    list_display = (
        'id',
        'province',
        'municipality',
        'noOfFarmers',
        'totalRiceArea',
        'irrigated',
        'rainfed',
        'upland'
    )

    list_filter = (
        'province',
        'municipality',
    )

    # Alphabetical Province name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "province":
            kwargs["queryset"] = Province.objects.all().order_by('provDesc')
        return super(CityMunicipalityProfileAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js', # jquery
            'js/rdims_ajax.js',       # project static folder
        )

# Register for admin view
admin.site.register(ProductionSupport, ProductionSupportAdmin)
admin.site.register(ExtensionService, ExtensionServiceAdmin)
admin.site.register(MachineryEquipment, MachineryEquipmentAdmin)
admin.site.register(FacilityInfrastructure, FacilityInfrastructureAdmin)
admin.site.register(FinancialAssistance, FinancialAssistanceAdmin)
admin.site.register(AewProfile, AewProfileAdmin)
admin.site.register(TrainingsAttended, TrainingsAttendedAdmin)
admin.site.register(TrainingsConducted, TrainingsConductedAdmin)
admin.site.register(ProvinceCoordinate, ProvinceCoordinateAdmin)
admin.site.register(CityCoordinate, CityCoordinateAdmin)
admin.site.register(RecognitionsAwardsReceived, RecognitionsAwardsReceivedAdmin)
admin.site.register(CityMunicipalityProfile, CityMunicipalityProfileAdmin)