from .models import location
from rest_framework.serializers import ModelSerializer


class LocationSerializers(ModelSerializer):
    class Meta:
        model = location
        fields = '__all__'
