from django.db import models

# Create your models here.
from rdims_project.files import years

from location.models import Province, City, Region

YEARS = years.YEARS

class ProductionSupport(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='production_support_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='production_support_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    yearDate = models.CharField(max_length=4, blank=False, help_text='Year', choices=YEARS)
    activityTitle = models.TextField(null=True, blank=True, help_text='Title of Activity', default=None)
    leadImplementer = models.CharField(max_length=200, null=True, blank=True, help_text='Lead Implementer', default=None)
    agencyName = models.CharField(max_length=250, null=True, blank=True, help_text='Name of Agency', default=None)
    category = models.CharField(max_length=250, null=True, blank=True, help_text='Category', default=None)
    subCategory = models.CharField(max_length=250, null=True, blank=True, help_text='Sub-Category', default=None)
    monthdayDate = models.CharField(max_length=50, null=True, blank=True, help_text='The month and day when the activity is conducted', default=None)
    noOfUnits = models.TextField(null=True, blank=True, help_text='Number of units', default=None)
    weightPerBag = models.TextField(null=True, blank=True, help_text='If category is seeds or fertilizer, specify weight', default=None)
    fertType = models.TextField(null=True, blank=True, help_text='If category is fertilizer, specify type', default=None)
    noOfRecipient = models.IntegerField(null=True, blank=True, help_text='Number of Farmer Recipients ', default=None)

    class Meta:
        ordering = ['province', 'municipality', 'yearDate', ]
        verbose_name = 'Production Support'
        verbose_name_plural = 'Production Support'    

    # def __str__(self):
    #     return f'{self.activityTitle}'

class ExtensionService(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='extension_service_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='extension_service_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    yearDate = models.CharField(max_length=4, blank=False, help_text='Year', choices=YEARS)
    activityTitle = models.TextField(null=True, blank=True, help_text='Title of Activity', default=None)    
    leadImplementer = models.CharField(max_length=200, null=True, blank=True, help_text='Lead Implementer', default=None)
    agencyName = models.CharField(max_length=250, null=True, blank=True, help_text='Name of Agency', default=None)
    category = models.CharField(max_length=250, null=True, blank=True, help_text='Category', default=None)
    subCategory = models.CharField(max_length=250, null=True, blank=True, help_text='Sub-Category', default=None)
    topics = models.CharField(max_length=500, null=True, blank=True, help_text='Topics', default=None)
    monthdayDate = models.CharField(max_length=50, null=True, blank=True, help_text='The month and day when the activity is conducted', default=None)
    duration = models.CharField(max_length=250, null=True, blank=True, help_text='Duration of the activity (Short-5days below, Long- longer than 5 days)', default=None)
    noOfFarmersServed = models.IntegerField(null=True, blank=True, help_text='Number of Farmer served by the activity', default=None)


    class Meta:
        ordering = ['province', 'municipality', 'yearDate', ]
        verbose_name = 'Extention Service'
        verbose_name_plural = 'Extension Service'

class MachineryEquipment(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='machinery_equipment_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='machinery_equipment_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    yearDate = models.CharField(max_length=4, blank=False, help_text='Year', choices=YEARS)
    activityTitle = models.TextField(null=True, blank=True, help_text='Title of Activity', default=None)
    leadImplementer = models.CharField(max_length=200, null=True, blank=True, help_text='Lead Implementer', default=None)
    agencyName = models.CharField(max_length=250, null=True, blank=True, help_text='Name of Agency', default=None)
    machEquipType = models.CharField(max_length=500, null=True, blank=True, help_text='Machinery Type', default=None)
    monthdayDate = models.CharField(max_length=50, null=True, blank=True, help_text='The month and day when the activity is conducted', default=None)
    noOfUnits = models.IntegerField(null=True, blank=True, help_text='Number of units distributed', default=None)
    fcaName = models.CharField(max_length=500, null=True, blank=True, help_text='Name of FCA', default=None)

    class Meta:
        ordering = ['province', 'municipality', 'yearDate', ]
        verbose_name = 'Machinery and Equipment'
        verbose_name_plural = 'Machinery and Equipment'

class FacilityInfrastructure(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='facility_infrastructure_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='facility_infrastructure_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    yearDate = models.CharField(max_length=4, blank=False, help_text='Year', choices=YEARS)
    projectTitle = models.TextField(null=True, blank=True, help_text='Project Title', default=None)
    fundSource = models.CharField(max_length=200, null=True, blank=True, help_text='Fund Source', default=None)
    amount = models.FloatField(null=True, blank=True, help_text='Amount', default=None)
    category = models.CharField(max_length=200, null=True, blank=True, help_text='Category', default=None)
    monthdayDate = models.CharField(max_length=50, null=True, blank=True, help_text='The month and day when the activity is conducted', default=None)
    faciInfraType = models.CharField(max_length=500, null=True, blank=True, help_text='Type of facility or Infrastructure', default=None)
    
    class Meta:
        ordering = ['province', 'municipality', 'yearDate', ]
        verbose_name = 'Facilities and Infrastructure'
        verbose_name_plural = 'Facilities and Infrastructure'

class FinancialAssistance(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='financial_assistance_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='financial_assistance_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    yearDate = models.CharField(max_length=4, blank=False, help_text='Year', choices=YEARS)
    activityTitle = models.TextField(null=True, blank=True, help_text='Title of Activity', default=None)
    leadImplementer = models.CharField(max_length=200, null=True, blank=True, help_text='Lead Implementer', default=None)
    agencyName = models.CharField(max_length=250, null=True, blank=True, help_text='Name of Agency', default=None)
    category = models.CharField(max_length=500, null=True, blank=True, help_text='Category', default=None)
    monthdayDate = models.CharField(max_length=50, null=True, blank=True, help_text='The month and day when the activity is conducted', default=None)
    totalAmount = models.FloatField(null=True, blank=True, help_text='Total amount', default=None)
    noOfFarmersAvailed = models.IntegerField(null=True, blank=True, help_text='The number of farmers benefited by the activity', default=None)
    
    class Meta:
        ordering = ['province', 'municipality', 'yearDate', ]
        verbose_name = 'Financial Assistance'
        verbose_name_plural = 'Financial Assistance'

class AewProfile(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='aew_profile_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='aew_profile_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    name = models.CharField(max_length=100, blank=False, help_text='Name', default=None)
    position = models.CharField(max_length=200, null=True, blank=True, help_text='Position', default=None)
    sex = models.CharField(max_length=50, null=True, blank=True, help_text='Sex', default=None)
    age = models.IntegerField(null=True, blank=True, default=None, help_text='Age')
    employmentStatus = models.CharField(max_length=100, null=True, blank=True, help_text='Employment Status', default=None)
    yearsInService = models.FloatField(null=True, blank=True, default=None, help_text='Years in Service')
    birthdate = models.DateField(null=True, blank=True, default=None, help_text='Birthdate')
    trainingsWanted = models.TextField(null=True, blank=True, help_text='Rice-related Trainings Wanted to Attend', default=None)
    remarks = models.CharField(max_length=50, null=True, blank=True, help_text='Status of AEW (Type Old, New, Resigned, or Retired Staff)', default=None)

    class Meta:
        ordering = ['province', 'municipality',]
        verbose_name = 'AEW Profile'
        verbose_name_plural = 'AEW Profile'

class TrainingsAttended(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='trainings_attended_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='trainings_attended_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    date = models.CharField(max_length=150, blank=True, null=True, help_text='Date')
    yearDate = models.CharField(max_length=4, blank=True, null=True, default=None, help_text='Year', choices=YEARS)
    activityTitle = models.TextField(null=True, blank=True, help_text='Title of Activity', default=None)
    topics = models.CharField(max_length=200, null=True, blank=True, help_text='Topics', default=None)
    trainingImplementer = models.CharField(max_length=2500, null=True, blank=True, help_text='Training Implementer', default=None)
    
    class Meta:
        ordering = ['province', 'municipality', 'yearDate', ]
        verbose_name = 'Trainings Attended'
        verbose_name_plural = 'Trainings Attended'

class TrainingsConducted(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='trainings_conducted_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='trainings_conducted_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    date = models.CharField(max_length=150, blank=True, null=True, help_text='Date')
    yearDate = models.CharField(max_length=4, blank=True, null=True, default=None, help_text='Year', choices=YEARS)
    activityTitle = models.TextField(null=True, blank=True, help_text='Title of Activity', default=None)
    topics = models.CharField(max_length=200, null=True, blank=True, help_text='Topics', default=None)
    
    class Meta:
        ordering = ['province', 'municipality', 'yearDate', ]
        verbose_name = 'Trainings Conducted'
        verbose_name_plural = 'Trainings Conducted'

class ProvinceCoordinate(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='province_coordinate_province', db_column='province', null=True, blank=True, db_constraint=False)
    coordinates = models.TextField(null=True, blank=True, help_text='Coordinates', default=None)
    
    class Meta:
        ordering = ['province',]
        verbose_name = 'Coordinates - Province'
        verbose_name_plural = 'Coordinates - Province'

class CityCoordinate(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='city_coordinate_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_coordinate_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    coordinates = models.TextField(null=True, blank=True, help_text='Coordinates', default=None)
    
    class Meta:
        ordering = ['province', 'municipality', ]
        verbose_name = 'Coordinates - City'
        verbose_name_plural = 'Coordinates - City'

class RecognitionsAwardsReceived(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='recognitions_awards_received_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='recognitions_awards_received_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    dateAwarded = models.CharField(max_length=20, blank=True, null=True, help_text='Date Awarded')
    titleOfAward = models.CharField(max_length=500, null=True, blank=True, help_text='Title of Award', default=None)
    awardingBody = models.CharField(max_length=300, null=True, blank=True, help_text='Awarding Body', default=None)
    category = models.CharField(max_length=50, blank=True, null=True, help_text='Category', default=None)
    awardeeName = models.CharField(max_length=50, blank=True, null=True, help_text='Awardee Name', default=None)

    class Meta:
        ordering = ['province', 'municipality', 'dateAwarded', ]
        verbose_name = 'Recognitions Awards Received'
        verbose_name_plural = 'Recognitions Awards Received'

class CityMunicipalityProfile(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='city_municipality_profile_province', db_column='province', null=True, blank=True, db_constraint=False)
    municipality = models.ForeignKey(City, on_delete=models.CASCADE, related_name='city_municipality_profile_municipality', db_column='municipality', null=True, blank=True, db_constraint=False)
    noOfFarmers = models.IntegerField(null=True, blank=True, default=None, help_text='Number of Farmers')
    totalRiceArea = models.FloatField(null=True, blank=True, default=None, help_text='Total Rice Area in Hectares (Physical)')
    irrigated = models.FloatField(null=True, blank=True, default=None, help_text='Irrigated')
    rainfed = models.FloatField(null=True, blank=True, default=None, help_text='Rainfed')
    upland = models.FloatField(null=True, blank=True, default=None, help_text='Upland')

    class Meta:
        ordering = ['province', 'municipality', ]
        verbose_name = 'City Municipality Profile'
        verbose_name_plural = 'City Municipality Profile'