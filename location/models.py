from django.db import models

# Create your models here.

class Region(models.Model):
    psgcCode =  models.CharField(max_length=50, null=True, blank=True, help_text="PSGC Code", default=None)
    regDesc = models.CharField(max_length=150, null=True, blank=True, help_text="Region Name", default=None)
    regCode = models.IntegerField(blank=False, help_text="Reg Code")
    population = models.CharField(max_length=50, null=True, blank=True, help_text="Population", default=None)

    def __str__(self):
        return self.regDesc

    class Meta:
        ordering = ['id']
        verbose_name = 'Region'
        verbose_name_plural = 'Region'

class Province(models.Model):
    psgcCode =  models.CharField(max_length=50, null=True, blank=True, help_text="PSGC Code", default=None)
    provDesc = models.CharField(max_length=150, null=True, blank=True, help_text="Province Name", default=None)
    regCode = models.ForeignKey(Region, on_delete=models.CASCADE, help_text="Region")
    provCode = models.IntegerField(blank=False, help_text="Provincial Code")
    population = models.CharField(max_length=50, null=True, blank=True, help_text="Population", default=None)

    def __str__(self):
        return self.provDesc

    class Meta:
        ordering = ['id']
        verbose_name = 'Province'
        verbose_name_plural = 'Province'

class City(models.Model):
    psgcCode =  models.CharField(max_length=50, null=True, blank=True, help_text="PSGC Code", default=None)
    cityDesc = models.CharField(max_length=150, null=True, blank=True, help_text="City Name", default=None)
    regCode = models.ForeignKey(Region, on_delete=models.CASCADE, help_text="Region")
    provId = models.ForeignKey(Province, on_delete=models.CASCADE, help_text="Province")
    provCode = models.IntegerField(blank=False, help_text="Provincial Code", editable=False)
    cityCode = models.IntegerField(blank=False, help_text="City Code")
    population = models.CharField(max_length=50, null=True, blank=True, help_text="Population", default=None)
    
    def __str__(self):
        return self.cityDesc

    def save(self, *args, **kwargs):
        if self.provId:
            self.provCode = Province.objects.get(id=self.provId.id).provCode
        super(City, self).save(*args, **kwargs)    

    class Meta:
        ordering = ['id']
        verbose_name = 'City'
        verbose_name_plural = 'City'