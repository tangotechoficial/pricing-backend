from .models import Campo, Sequencia, CampoSequencia, TipoValor, ChaveContas, Camada, Condicao, SequenciaCondicao, EsquemaDeCalculo, CondicaoCamadaEsquema
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

""" class SEQUENCIACAMPOSerializer(serializers.ModelSerializer):
    campos = serializers.SerializerMethodField()

    class Meta:
        model = Sequencia
        fields = '__all__'

    def get_campos(self, obj):
        campos = Campo.objects.filter(sequencia=obj)
        return CampoSerializer(campos, many=True).data

class SEQ_AUXSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEQ_AUX
        fields = '__all__'

class CHAVE_CONTASSerializer(serializers.ModelSerializer):
    class Meta:
        model = CHAVE_CONTAS
        fields = '__all__'

class TIPOVALORSerializer(serializers.ModelSerializer):
    class Meta:
        model = TIPOVALOR
        fields = '__all__'

class CONDICAOSerializer(serializers.ModelSerializer):
    class Meta:
        model = CONDICAO
        fields = '__all__'

class CONDICAOSEQSerializer(serializers.ModelSerializer):
    sequencias = serializers.SerializerMethodField()
    chavecontas = serializers.SerializerMethodField()
    tipovalor = serializers.SerializerMethodField()

    class Meta:
        model = CONDICAO
        fields = '__all__'

    def get_sequencias(self, obj):
        sequencias = SEQUENCIA.objects.filter(condicao=obj)
        return SEQUENCIACAMPOSerializer(sequencias, many=True).data
    
    def get_chavecontas(self, obj):
        chavecontas = CHAVE_CONTAS.objects.filter(condicao=obj)
        return CHAVE_CONTASSerializer(chavecontas, many=True).data
    
    def get_tipovalor(self, obj):
        tipovalor = TIPOVALOR.objects.filter(condicao=obj)
        return TIPOVALORSerializer(tipovalor, many=True).data


class CAMADASerializer(serializers.ModelSerializer):
    class Meta:
        model = CAMADA
        fields = ['Cod_Camada', 'Nome_Camada', 'TIPO_BASE_VENDAS']

class CAMADACONDSerializer(serializers.ModelSerializer):
    condicaos = serializers.SerializerMethodField()

    class Meta:
        model = CAMADA
        fields = ['Cod_Camada', 'Nome_Camada', 'TIPO_BASE_VENDAS', 'condicaos']

    def get_condicaos(self, obj):
        condicaos = CONDICAO.objects.filter(Cod_Camada=obj.Cod_Camada)
        return CONDICAOSEQSerializer(condicaos, many=True).data
    
class CONDICAO_SEQUENCIASerializer(serializers.ModelSerializer):
    class Meta:
        model = CONDICAO_SEQUENCIA
        fields = '__all__'

class ESQUEMA_DE_CALCULOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESQUEMA_DE_CALCULO
        fields = '__all__'

class PRECOSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRECO
        fields = '__all__'

class CONDICAO_CAMADA_ESQUEMASerializer(serializers.ModelSerializer):
    class Meta:
        model = CONDICAO_CAMADA_ESQUEMA
        fields = '__all__'

class MERCADORIASerializer(serializers.ModelSerializer):
    class Meta:
        model = MERCADORIA
        fields = '__all__'

class FILIALSerializer(serializers.ModelSerializer):
    class Meta:
        model = FILIAL
        fields = '__all__'

class FATURAMENTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = FATURAMENTO
        fields = '__all__'

class ESTADOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESTADO
        fields = '__all__'

class REGIONSerializer(serializers.ModelSerializer):
    class Meta:
        model = REGION
        fields = '__all__' """