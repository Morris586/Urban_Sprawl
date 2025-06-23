import csv
import os
from django.http import HttpResponse
from django.shortcuts import render
from .models import Pollution, Deforestation, UrbanSprawl
from collections import defaultdict
from django.conf import settings 


def pollution_list(request):#csv file export
    search_query = request.GET.get('search', '')
    year_filter = request.GET.get('year', '')

    pollution_data = Pollution.objects.all().order_by('year')

    if search_query:
        pollution_data = pollution_data.filter(name__icontains=search_query)

    if year_filter:
        try:
            year_filter = int(year_filter)
            pollution_data = pollution_data.filter(year=year_filter)
        except ValueError:
            pass

    context = {
        'pollution_data': pollution_data,
        'search_query': search_query,
        'year_filter': year_filter,
    }
    return render(request, 'gis_app/pollution_list.html', context)


def pollution_export(request):
    search_query = request.GET.get('search', '')
    year_filter = request.GET.get('year', '')

    pollution_data = Pollution.objects.all()

    if search_query:
        pollution_data = pollution_data.filter(name__icontains=search_query)

    if year_filter:
        try:
            year_filter = int(year_filter)
            pollution_data = pollution_data.filter(year=year_filter)
        except ValueError:
            pass

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pollution_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Year', 'Air Quality Index', 'Waste Generation', 'Location'])

    for item in pollution_data:
        writer.writerow([item.name, item.year, item.air_quality_index, item.waste_generation, item.location])

    return response


def deforestation_list(request):
    search_query = request.GET.get('search','')
    year_filter = request.GET.get('year', '')

    deforestation_data = Deforestation.objects.all().order_by('year')

    if search_query:
        deforestation_data = deforestation_data.filter(name__icontains=search_query)

    if year_filter:
        try:
            year_filter = int(year_filter)
            deforestation_data = deforestation_data.filter(year=year_filter)
        except ValueError:
            pass

    context = {
        'deforestation_data': deforestation_data,
        'search_query': search_query,
        'year_filter': year_filter,
    }
    return render(request, 'gis_app/deforestation_list.html', context)

def deforestation_export(request):
    search_query = request.GET.get('search', '')
    year_filter = request.GET.get('year', '')

    deforestation_data = Deforestation.objects.all()

    if search_query:
        deforestation_data = deforestation_data.filter(name__icontains=search_query)

    if year_filter:
        try:
            year_filter = int(year_filter)
            deforestation_data = deforestation_data.filter(year=year_filter)
        
        except ValueError:
            pass

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Deforestation_data.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Year', 'Forest Area Lost (sq km)', 'location'])

    for item in deforestation_data:
        writer.writerow([item.name, item.year, item.forest_area_lost, item.location])
    return response




def urban_sprawl_list(request):
   search_query = request.GET.get('search', '')
   year_filter = request.GET.get('year', '')

   urban_sprawl_data = UrbanSprawl.objects.all().order_by('-year')

   if search_query:
       urban_sprawl_data = urban_sprawl_data.filter(name__icontains=search_query)

   if year_filter:
       try:
           year_filter = int(year_filter)
           urban_sprawl_data = urban_sprawl_data.filter(year=year_filter)

       except ValueError:
           pass
       
   context = {
           'urban_sprawl_data': urban_sprawl_data,
           'search_query': search_query,
           'year_filter': year_filter,
       }
   return render(request, 'gis_app/urban_sprawl_list.html', context)

def urban_sprawl_export(request):
    search_query = request.GET.get('search', '')
    year_filter = request.GET.get('year', '')

    urban_sprawl_data = UrbanSprawl.objects.all()

    if search_query:
        urban_sprawl_data = urban_sprawl_data.filter(name__icontains=search_query)
    
    if year_filter:
        try:
            year_filter = int(year_filter)
            urban_sprawl_data = urban_sprawl_data.filter(year=year_filter)

        except ValueError:
            pass

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename= "urban_sprawl_data.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Name', 'Year', 'Urban Area Increase (%)', 'Location'])

    for item in urban_sprawl_data:
        writer.writerow([item.name, item.year, item.urban_area_increase, item.location])

    return response


def map_view(request):
    urban_file = os.path.join(settings.BASE_DIR, 'gis_app','static','gis_app','data','urban_sprawl_data.csv')
    deforestation_file = os.path.join(settings.BASE_DIR, 'gis_app','static','gis_app','data','deforestation_data.csv')

    urban_totals = 0
    forest_totals = 0

    urban_by_year = defaultdict(float)
    deforestation_by_year = defaultdict(float)

    with open(urban_file, 'r') as file:  #reads urban sprawl data
        reader = csv.DictReader(file)
        for row in reader:
            year = row['year']
            area = float(row['urban_area'])
            urban_totals += area
            urban_by_year[year] += area

    with open(deforestation_file, 'r') as file: # reads deforestation data
        reader = csv.DictReader(file)
        for row in reader:
            year = row['year']
            loss = float(row['forest_cover_loss'])
            forest_totals += loss
            deforestation_by_year[year] += loss

    context = {
        'urban_totals': urban_totals,
        'urban_by_year': dict(urban_by_year),
        'forest_totals': forest_totals,
        'forest_by_year': dict(deforestation_by_year),
    }

   



    return render(request, 'gis_app/index.html', context) # This is the main map view page.  

def summary_view(request): #loads csv files 
    urban_file = os.path.join(settings.BASE_DIR, 'gis_app', 'static', 'gis_app', 'data', 'urban_sprawl_data.csv')
    deforestation_file = os.path.join(settings.BASE_DIR, 'gis_app', 'static', 'gis_app', 'data', 'deforestation_data.csv')

    urban_values = []# list to store values
    deforestation_values = []

    with open(urban_file, 'r') as file: # reads urban_sprawl data
        reader = csv.DictReader(file)
        for row in reader:
            urban_values.append(float(row['urban_area']))

    with open(deforestation_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            deforestation_values.append(float(row['forest_cover_loss']))

    summary={
        'urban': {
            'max': max(urban_values),
            'min': min(urban_values),
            'average': sum(urban_values) / len(urban_values) if urban_values else 0,
        },
        'deforestation': {
            'max': max(deforestation_values),
            'min': min(deforestation_values),
            'average': sum(deforestation_values) / len(deforestation_values) if deforestation_values else 0,
        }
    }
    return render(request, 'gis_app/summary.html', {'summary': summary})


def help_view(request):
    return render(request, 'gis_app/help.html') #The help page 






# Create your views here.
