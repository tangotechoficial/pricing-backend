from rest_framework import serializers
from . import models

class BasePrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasePreco
        fields = '__all__'

class MovplncmpcalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movplncmpcal
        fields = '__all__'