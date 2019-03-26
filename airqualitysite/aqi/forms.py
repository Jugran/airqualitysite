from django import forms

from .models import City, Location, Station


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('country', 'city', 'station')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['city'].queryset = City.objects.none()
        self.fields['station'].queryset = Station.objects.none()
