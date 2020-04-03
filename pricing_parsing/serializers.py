from rest_framework import serializers
from . import models

class MovplncmpcalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movplncmpcal
        fields = '__all__'