from django.contrib import admin
from .models import Country, City, Station


# Register your models here.
class StationsInline(admin.TabularInline):
    model = Station
    ordering = ['name']
    extra = 0


class CitiesInline(admin.TabularInline):
    model = City
    ordering = ['name']
    extra = 0


class CountryAdmin(admin.ModelAdmin):
    inlines = [CitiesInline]
    list_display = ['name', 'code']
    ordering = ['name']


admin.site.register(Country, CountryAdmin)