from .models import Campo, Sequencia, CampoSequencia, TipoValor, ChaveContas, Camada, Condicao, SequenciaCondicao, EsquemaDeCalculo, CondicaoCamadaEsquema, FilialExpedicao, FilialFaturamento, Estado, Regiao, Mercadoria, ChavePrecificao, Preco, CodterchvCodcnl
from rest_framework import serializers
from pprint import pprint
## pprint(vars(OBJ))

class CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campo
        fields = '__all__'

class CampoSequenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoSequencia
        fields = '__all__'

class SequenciaSerializer(serializers.ModelSerializer):
    campos = serializers.SerializerMethodField()

    class Meta:
        model = Sequencia
        fields = '__all__'
    
    def get_campos(self, obj):
        vals = []
        campossequencia = CampoSequencia.objects.filter(cod_sequencia=obj.cod_sequencia)
        for c in campossequencia:
            campo = Campo.objects.get(cod_campo=c.cod_campo_id)
            vals.append(campo)
        return CampoSerializer(vals, many=True).data

class SequenciaCondicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SequenciaCondicao
        fields = '__all__'

class TipoValorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoValor
        fields = '__all__'

class ChaveContasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChaveContas
        fields = '__all__'

class CamadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camada
        fields = '__all__'

class CondicaoSerializer(serializers.ModelSerializer):
    sequencias = serializers.SerializerMethodField()

    class Meta:
        model = Condicao
        fields = '__all__'

    def get_sequencias(self, obj):
        vals = []
        sequenciascondicao = SequenciaCondicao.objects.filter(cod_condicao=obj.cod_condicao)
        for s in sequenciascondicao:
            sequencia = Sequencia.objects.get(cod_sequencia=s.cod_sequencia_id)
            vals.append(sequencia)
        return SequenciaSerializer(vals, many=True).data

class EsquemaDeCalculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EsquemaDeCalculo
        fields = '__all__'

class CondicaoCamadaEsquemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondicaoCamadaEsquema
        fields = '__all__'

class FilialExpedicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilialExpedicao
        fields = '__all__'

class FilialFaturamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilialFaturamento
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class RegiaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regiao
        fields = '__all__'

class MercadoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercadoria
        fields = '__all__'

class ChavePrecificaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChavePrecificao
        fields = '__all__'

class PrecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preco
        fields = '__all__'

class CamadaCondicaoSerializer(serializers.ModelSerializer):
    condicaos = serializers.SerializerMethodField()
    class Meta:
        model = Camada
        fields = '__all__'

    def get_condicaos(self, obj):
        condicaos = Condicao.objects.filter(cod_camada=obj.cod_camada)
        return CondicaoSerializer(condicaos, many=True).data

class EsquemaRelationSerializer(serializers.ModelSerializer):
    camadas = serializers.SerializerMethodField()

    class Meta:
        model = EsquemaDeCalculo
        fields = '__all__'

    def get_camadas(self, obj):
        camadas = Camada.objects.filter(tipo_base_vendas=obj.tipo_base_vendas)
        return CamadaCondicaoSerializer(camadas, many=True).data

class CodterchvCodcnlSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodterchvCodcnl
        fields = '__all__'