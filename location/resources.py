from import_export import resources, fields
from .models import Region, Province, City

class RegionResource(resources.ModelResource):
    class Meta:
        model = Region
        # header in csv file
        fields = (  
                    'id',   
                    'psgcCode',
                    'regDesc',
                    'regCode',
                    'population',
                )

class ProvinceResource(resources.ModelResource):
    class Meta:
        model = Province
        # header in csv file
        fields = (  
                    'id',   
                    'psgcCode',
                    'provDesc',
                    'regCode',
                    'provCode',
                    'population',
                )

    def before_import_row(self, row, **kwargs):
        try:
            if row['population'] == r'':
                row['population'] = ''
        except Exception as e:
            print(e)
        return row

class CityResource(resources.ModelResource):
    class Meta:
        model = City
        # header in csv file
        fields = (  
                    'id',   
                    'psgcCode',
                    'cityDesc',
                    'regCode',
                    'provId',
                    'provCode',
                    'cityCode',
                    'population',
                )

    def before_import_row(self, row, **kwargs):
        try:
            if row['population'] == r'':
                row['population'] = ''
        except Exception as e:
            print(e)
        return row