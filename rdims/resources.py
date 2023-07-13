from import_export import resources, fields
from .models import ProductionSupport, ExtensionService, MachineryEquipment, FacilityInfrastructure, FinancialAssistance, AewProfile, TrainingsAttended, TrainingsConducted, ProvinceCoordinate, CityCoordinate, RecognitionsAwardsReceived, CityMunicipalityProfile

from location.models import Province, City

class ProductionSupportResource(resources.ModelResource):
    class Meta:
        model = ProductionSupport
        # header in csv file
        fields = (  
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

    def before_import_row(self, row, **kwargs):
        try:
            if isinstance(row['province'], int) == False:
                row['province'] = Province.objects.filter(provDesc__icontains=row['province']).first().id
            province_id = row['province']

            if isinstance(row['municipality'], int) == False:
                if province_id is None:
                    row['municipality'] = City.objects.filter(cityDesc__icontains=row['municipality']).first().id
                else:
                    row['municipality'] = City.objects.filter(cityDesc__icontains=row['municipality'], provId=province_id).first().id

            if row['yearDate'] == r'Undetermined':
                row['yearDate'] = '0000'
            elif row['yearDate'] == r'No data':
                row['yearDate'] = '0000'
            elif row['yearDate'] == r'No Data':
                row['yearDate'] = '0000'
            elif row['yearDate'] == r'None':
                row['yearDate'] = '0000'
            elif row['yearDate'] == r'':
                row['yearDate'] = '0000'
        except Exception as e:
            print(e)
        return row

class ExtensionServiceResource(resources.ModelResource):
    class Meta:
        model = ExtensionService
        # header in csv file
        fields = (  
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
    
    def before_import_row(self, row, **kwargs):
        try:
            if row['yearDate'] == r'Undetermined':
                row['yearDate'] = '0000'
            elif row['yearDate'] == r'No data':
                row['yearDate'] = '0000'
            elif row['yearDate'] == r'No date':
                row['yearDate'] = '0000'
        except Exception as e:
            print(e)
        return row

class MachineryEquipmentResource(resources.ModelResource):
    class Meta:
        model = MachineryEquipment
        # header in csv file
        fields = (  
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

    def before_import_row(self, row, **kwargs):
        try:
            if row['yearDate'] == r'Undetermined':
                row['yearDate'] = '0000'
            elif row['yearDate'] == r'No data':
                row['yearDate'] = '0000'
        except Exception as e:
            print(e)
        return row

class FacilityInfrastructureResource(resources.ModelResource):
    class Meta:
        model = FacilityInfrastructure
        # header in csv file
        fields = (  
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
    def before_import_row(self, row, **kwargs):
        try:
            if row['amount'] == r'Undetermined':
                row['amount'] = 0.0
            elif row['amount'] == r'No data':
                row['amount'] = 0.0
            elif row['amount'] == r'':
                row['amount'] = 0.0    

            if row['yearDate'] == r'Undetermined':
                row['yearDate'] = '0000'
            elif row['yearDate'] == r'No data':
                row['yearDate'] = '0000'
        except Exception as e:
            print(e)
        return row

class FinancialAssistanceResource(resources.ModelResource):
    class Meta:
        model = FinancialAssistance
        # header in csv file
        fields = (  
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

class AewProfileResource(resources.ModelResource):
    class Meta:
        model = AewProfile
        # header in csv file
        fields = (  
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

class TrainingsAttendedResource(resources.ModelResource):
    class Meta:
        model = TrainingsAttended
        # header in csv file
        fields = (  
                    'id',   
                    'province',
                    'municipality',
                    'date',
                    'yearDate',
                    'activityTitle',
                    'topics',
                    'trainingImplementer'
                )

class TrainingsConductedResource(resources.ModelResource):
    class Meta:
        model = TrainingsConducted
        # header in csv file
        fields = (  
                    'id',   
                    'province',
                    'municipality',
                    'date',
                    'yearDate',
                    'activityTitle',
                    'topics'
                )

class ProvinceCoordinateResource(resources.ModelResource):
    class Meta:
        model = ProvinceCoordinate
        # header in csv file
        fields = (  
                    'id',   
                    'province',
                    'coordinates'
                )

class CityCoordinateResource(resources.ModelResource):
    class Meta:
        model = CityCoordinate
        # header in csv file
        fields = (  
                    'id',   
                    'province',
                    'municipality',
                    'coordinates'
                )

class RecognitionsAwardsReceivedResource(resources.ModelResource):
    class Meta:
        model = RecognitionsAwardsReceived
        # header in csv file
        fields = (  
                    'id',   
                    'province',
                    'municipality',
                    'dateAwarded',
                    'titleOfAward',
                    'awardingBody',
                    'category',
                    'awardeeName'
                )

class CityMunicipalityProfileResource(resources.ModelResource):
    class Meta:
        model = CityMunicipalityProfile
        # header in csv file
        fields = (  
                    'id',   
                    'province',
                    'municipality',
                    'noOfFarmers',
                    'totalRiceArea',
                    'irrigated',
                    'rainfed',
                    'upland'
                )