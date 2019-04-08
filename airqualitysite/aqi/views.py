from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from . import forms
from .fetch import get_data
from .models import Location, City, Station, Country
from .populate import populate_stations


from rest_framework import generics
from .serializers import Serializer

# Create your views here.


class ListCreate(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = Serializer


class LocationForm(CreateView):
    model = Location
    form_class = forms.LocationForm


def get_location(request):
    if request.method == 'POST':
        form = forms.LocationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.values()
            print(data, type(data))
            return HttpResponse(str(data))
        else:
            return HttpResponse('Invalid Form data')
    else:
        return HttpResponse('No post data')


def load_cities(request):
    print('loading cities')
    country_code = request.GET.get('country')
    cities = City.objects.filter(country=country_code).order_by('name')
    return render(request, 'aqi/city_dropdown.html', {'cities': cities})


def load_stations(request):
    print('loading stations')
    city_pk = request.GET.get('city')
    stations = Station.objects.filter(city=city_pk).order_by('name')
    return render(request, 'aqi/station_dropdown.html', {'stations': stations})


def populate(request):
    return populate_stations(request)


def measurements(request):
    req = request.POST
    city = get_object_or_404(City, pk=req['city'])
    station = get_object_or_404(Station, pk=req['station'])

    params = 'country={COUNTRY}&city={CITY}&location={STATION}'.format(
        COUNTRY=req['country'], CITY=city.name, STATION=station.name)
    print(params)

    data = get_data('latest', params)
    print(data)
    return render(request, 'aqi/measurements.html', {'data': data})
