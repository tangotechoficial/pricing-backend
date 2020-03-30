from rest_framework import serializers

from django.contrib.auth.models import User

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'groups')

class FornecedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Fornecedor
        fields = '__all__'

class CompradorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Comprador
        fields = '__all__'

class TabAuxGrpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TabAuxGrp
        fields = '__all__'

class RelacionamentoFilialRegiaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RelacionamentoFilialRegiao
        fields = '__all__'''

class MercadoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Mercadoria
        fields = '__all__'

class RepresentanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Representante
        fields = '__all__'

class VendasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Vendas
        fields = '__all__'

class VerbaeBCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VerbaeBC
        fields = '__all__'

class ElasticidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Elasticidade
        fields = '__all__'

class EstoqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Estoque
        fields = '__all__'

class CompetitividadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Competitividade
        fields = '__all__'

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

