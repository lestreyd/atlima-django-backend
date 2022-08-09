from rest_framework.serializers import ModelSerializer
from core.models.system import SystemLanguage


class SystemLanguageSerializer(ModelSerializer):
    """Model serializer for :model:SystemLanguage"""
    class Meta:
        model = SystemLanguage
        fields = '__all__'
