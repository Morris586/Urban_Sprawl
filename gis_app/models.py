from django.contrib.gis.db import models

class UrbanSprawl(models.Model):
    name = models.CharField(max_length=100, help_text="Location name e.g., Dandora", default = "Unknown")
    year = models.FloatField()
    urban_area = models.FloatField()
    population_density = models.FloatField()
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.name
    
class Deforestation(models.Model):
    name = models.CharField(max_length=100, help_text="Location name e.g., Dandora", default = "Unknown")
    year = models.IntegerField()
    forest_cover_loss = models.FloatField(help_text="Amount lost (in hectares)")
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.name
    
class Pollution(models.Model):
    name = models.CharField(max_length=100, help_text="Location name e.g., Dandora", default= "Unknown")
    year = models.IntegerField()
    air_quality_index = models.FloatField()
    waste_generation = models.FloatField()
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.name


# Create your models here.
