from django.urls import path
from . import views

urlpatterns = [
    path('pollution/', views.pollution_list, name='pollution_list'),
    path('pollution/export/', views.pollution_export, name='pollution_export'),

    path('deforestation/', views.deforestation_list, name='deforestation_list'),
    path('deforestation/export/', views.deforestation_export, name='deforestation_export'),

    path('urban_sprawl/export/', views.urban_sprawl_export, name='urban_sprawl_export'),
    path('urban_sprawl/', views.urban_sprawl_list, name='urban_sprawl_list'),

    path('', views.map_view, name = 'map_view'),
   path('summary/', views.summary_view, name='summary'),
   path('help/', views.help_view, name='help_page'), 
]