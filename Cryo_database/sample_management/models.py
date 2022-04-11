from django.db import models

# Create your models here.
class Sample(models.Model):
    hp_accession = models.CharField(max_length = 10)
    patient_id = models.CharField(max_length = 10)
    collection_date = models.DateField('date_collected')
    specimen_type =models.CharField(max_length=100) #required - consider using model choices
    specimen_description = models.CharField(max_length = 100)
    morph_dx = models.CharField(max_length=250) #use choices here as well?
    interpretation = models.TextField(max_length = 500)
    comment = models.TextField(max_length = 500)
    def __str__(self):
        return self.hp_accession


class Location(models.Model):
    #Frozen Amps = count of entries in location
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
    tank = models.CharField(max_length = 20)
    rack = models.CharField(max_length = 20)
    pie = models.CharField(max_length = 20)
    cell_count = models.CharField(max_length = 20) #required

    class Meta:
        unique_together = ('tank', 'rack', 'pie')
    
    def __str__(self):
            return f"Tank: {self.tank}, Rack: {self.rack}, Pie: {self.pie}"

