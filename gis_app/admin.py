from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from.models import UrbanSprawl, Deforestation, Pollution

@admin.register(UrbanSprawl)
class UrbanSprawlAdmin(GISModelAdmin):
    list_display = ('name','year', 'urban_area', 'population_density', 'location')
    list_filter = ('year',)
    ordering = ('-year',)
    default_lon = 36.8219
    default_lat = -1.2921
    default_zoom = 10

@admin.register(Deforestation)
class DeforestationAdmin(GISModelAdmin):
    list_display = ('name', 'year', 'forest_cover_loss', 'location')
    list_filter = ('year',)
    ordering = ('-year',)
    default_lon = 36.8219
    default_lat = -1.2921
    default_zoom = 10

@admin.register(Pollution)
class PollutionAdmin(GISModelAdmin):
    list_display = ('name', 'year', 'air_quality_index', 'waste_generation', 'location')
    list_filter = ('year',)
    search_fields = ('name',)
    ordering = ('-year',)
    default_lon = 36.8219   # Default longitude (Nairobi center)
    default_lat = -1.2921   # Default latitude (Nairobi center)
    default_zoom = 10

    fieldsets = (
        (None, {
            'fields': ('name', 'year')
        }),
        ('Pollution Stats', {
            'fields': ('air_quality_index', 'waste_generation')
        }),
        ('Location', {
            'fields': ('location',)
        }),
    )