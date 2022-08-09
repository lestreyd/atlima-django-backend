from rest_framework import serializers
from core.models import Region
from core.models import Content

class RegionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Region
        fields = '__all__'