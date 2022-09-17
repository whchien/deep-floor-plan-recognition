from rest_framework import serializers
from api.models import RawImageModel


class RawImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawImageModel
        fields = '__all__'