from rest_framework import serializers

from django.contrib.auth.models import User, Group

from . import models


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'groups')

class DadosMestre_VerbaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DadosMestre_Verba
        fields = '__all__'

class DadosMestre_VerbaCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DadosMestre_VerbaCSV
        fields = ['import_date']

class DadosMestre_ComposicaoPrecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DadosMestre_ComposicaoPreco
        fields = '__all__'

class DadosMestre_ComposicaoPrecoCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DadosMestre_ComposicaoPrecoCSV
        fields = ['import_date']

class DiretrizesEstrategicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DiretrizesEstrategica
        fields = '__all__'

class DiretrizesEstrategicaCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DiretrizesEstrategicaCSV
        fields = ['import_date']

class PlanoComprasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PlanoCompras
        fields = '__all__'

class OtimizadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Otimizador
        fields = '__all__'
