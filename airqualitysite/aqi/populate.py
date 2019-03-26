from django.db import IntegrityError
from django.shortcuts import get_object_or_404, HttpResponse

from .models import Country, City, Station
from.fetch import get_data

def populate_data(request):
    countries = get_data('countries')

    for country in countries:
        country_model = Country(code=country[0], name=country[1])
        print(str(country))
        try:
            country_model.save()
        except IntegrityError:
            print('Skipping duplicate entry! ')

        cities = get_data('cities', 'country=%s' % country[0])
        print(len(cities))
        if len(cities) > 0:
            for city in cities:
                country_key = get_object_or_404(Country, pk=country[0])
                city = City(name=city, country=country_key)
                try:
                    city.save()
                    print(str(city))
                except IntegrityError:
                    print('Skipping duplicate entry! ')

    return HttpResponse('Updated!')


def populate_stations(request):
    country_id = 'IN'
    country_pk = get_object_or_404(Country, pk=country_id)

    cities = get_data('cities', 'country=%s' % country_id)

    for city in cities:
        city_pk = get_object_or_404(City, name=city)
        assert city_pk is not None, "No city returned"

        param = 'country={COUNTRY}&city={CITY}'.format(COUNTRY=country_id, CITY=city)
        stations = get_data('locations', param)

        for station in stations:
            station_model = Station(name=station, city=city_pk, country=country_pk)
            try:
                print(station_model, country_pk, city_pk)
                station_model.save()
            except IntegrityError:
                print('Skipping duplicate entry! ')

    return HttpResponse('Updated!')
