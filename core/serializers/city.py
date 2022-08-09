from rest_framework import serializers
from core.models.city import City
from .content import ContentSerializer

class CitySerializer():
    content = ContentSerializer()
    class Meta:
        model = City
        fields = '__all__'