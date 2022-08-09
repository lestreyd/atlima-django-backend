from rest_framework import serializers
from core.models.country import Country
from .content import ContentSerializer

class CountrySerializer():
    content = ContentSerializer()
    class Meta:
        model = Country
        fields = '__all__'