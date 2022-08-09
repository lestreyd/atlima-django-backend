from rest_framework.serializers import ModelSerializer

class UserSerializer (ModelSerializer):
    class Meta:
        fields = '__all__'