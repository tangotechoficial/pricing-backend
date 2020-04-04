from rest_framework import serializers
from . import models

class BasePrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BasePreco
        fields = '__all__'

class CompetitividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competitividade
        fields = '__all__'

class ElasticidadeDemandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ElasticidadeDemanda
        fields = '__all__'

class EttprdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ettprd
        fields = '__all__'

class MetasdiariasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Metasdiarias
        fields = '__all__'

class MovetqSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movetq
        fields = '__all__'

class MovplncmpcalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movplncmpcal
        fields = '__all__'
        
class MovvbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movvbs
        fields = '__all__'

class MovvndhstfimSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movvndhstfim
        fields = '__all__'

class OutputPlnSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OutputPln
        fields = '__all__'

class PrdsmlSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prdsml
        fields = '__all__'