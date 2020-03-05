from .models import DadosMestre, DadosMestreCSV, DiretrizesEstrategica, DiretrizesEstrategicaCSV
from rest_framework import serializers


class DadosMestreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DadosMestre
        fields = '__all__'

class DadosMestreCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DadosMestreCSV
        fields = ['import_date']

class DiretrizesEstrategicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiretrizesEstrategica
        fields = '__all__'

class DiretrizesEstrategicaCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiretrizesEstrategicaCSV
        fields = ['import_date']
