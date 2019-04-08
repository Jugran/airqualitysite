from django.urls import path


from . import views

app_name = 'aqi'

urlpatterns = [
    path('api/Country', views.ListCreate.as_view()),
    path('', views.LocationForm.as_view(), name='location_form'),
    path('measurements', views.measurements, name='measurements'),
    path('ajax/load_cities', views.load_cities, name='ajax_load_cities'),
    path('ajax/load_locations', views.load_stations, name='ajax_load_locations'),
    path('populate', views.populate, name='populate_data'),

]
