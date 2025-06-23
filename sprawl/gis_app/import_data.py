import csv 
from django.contrib.gis.geos import Point
from gis_app.models import UrbanSprawl, Deforestation

def import_urban_sprawl_data(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            UrbanSprawl.objects.create(
                name=row['name'],
                year=int(row['year']),
                urban_area=float(row['urban_area']),
                population_density=float(row['population_density']),
                location=Point(float(row['longitude']), float(row['latitude']))
            )
    print("Urban Sprawl data imported successfully")

def import_deforestation_data(csv_path):
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Deforestation.objects.create(
                name = row['name'],
                year = int(row['year']),
                forest_cover_loss = float(row['forest_cover_loss']),
                location = Point(float(row['longitude']), float(row['latitude']))

            )
    print("Deforestation data imported successfully")
