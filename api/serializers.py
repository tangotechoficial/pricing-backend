from rest_framework import serializers

from django.contrib.auth.models import User

from .models import (DadosMestre_Verba, DadosMestre_VerbaCSV,
                     DadosMestre_ComposicaoPreco, DadosMestre_ComposicaoPrecoCSV,
                     DiretrizesEstrategica, DiretrizesEstrategicaCSV)


class DadosMestre_VerbaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DadosMestre_Verba
        fields = '__all__'

class DadosMestre_VerbaCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DadosMestre_VerbaCSV
        fields = ['import_date']

class DadosMestre_ComposicaoPrecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DadosMestre_ComposicaoPreco
        fields = '__all__'

class DadosMestre_ComposicaoPrecoCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DadosMestre_ComposicaoPrecoCSV
        fields = ['import_date']

class DiretrizesEstrategicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiretrizesEstrategica
        fields = '__all__'

class DiretrizesEstrategicaCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiretrizesEstrategicaCSV
        fields = ['import_date']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'groups')
