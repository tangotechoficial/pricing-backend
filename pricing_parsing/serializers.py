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


class EttprdFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ettprd
        fields = ['desprd', 'codprd']


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


class DadosMestre_VerbaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DadosMestre_Verba
        fields = '__all__'


class ElasticidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Elasticidade
        fields = '__all__'


class VerbaeBCSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VerbaeBC
        fields = '__all__'


class VendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendas
        fields = '__all__'


class DadosMestre_ComposicaoPrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DadosMestre_ComposicaoPreco
        fields = '__all__'


class DiretrizesEstrategicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiretrizesEstrategica
        fields = '__all__'


class DiretrizesFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiretrizesEstrategica
        fields = ['DESDRTCLLATU', 'CODGRPMER', 'DESGRPMER', 'CODFMLMER', 'DESFMLMER',
                  'CODCLSMER', 'DESCLSMER', 'CODDIVFRN', 'NOMFRN', 'CODFIL', 'CODESTUNI']

class DiretrizesFilterDirectoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiretrizesEstrategica
        fields = ['DESDRTCLLATU']

class DiretrizesFilterGroupMerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiretrizesEstrategica
        fields = ['CODGRPMER', 'DESGRPMER']

class DiretrizesFilterCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiretrizesEstrategica
        fields = ['CODFMLMER', 'DESFMLMER']

class DiretrizesFilterSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiretrizesEstrategica
        fields = ['CODCLSMER', 'DESCLSMER']

class DiretrizesFilterFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiretrizesEstrategica
        fields = ['CODDIVFRN', 'NOMFRN']

class DiretrizesFilterFilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DiretrizesEstrategica
        fields = ['CODESTUNI']

class PlanoComprasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlanoCompras
        fields = '__all__'

class PlanoComprasFilterFilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlanoCompras
        fields = ['CODFILEPD']

class PlanoComprasFilterFaturamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlanoCompras
        fields = ['CODFILFAT']

class PlanoComprasFilterUFSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlanoCompras
        fields = ['CODESTUNI']

class PlanoComprasFilterProdutoSerializer(serializers.ModelSerializer):
    DESPRD = serializers.SerializerMethodField()
    class Meta:
        model = models.PlanoCompras
        fields = ['CODPRD', 'DESPRD']
    
    def get_DESPRD(self, obj):
        return models.Ettprd.objects.values('desprd').filter(codprd=obj.CODPRD)[0]['desprd']

