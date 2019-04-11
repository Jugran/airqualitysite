from rest_framework import serializers
from .models import Country


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
