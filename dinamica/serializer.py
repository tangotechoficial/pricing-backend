from .models import SEQ_CAMPO, SEQUENCIA, SEQ_AUX, CHAVE_CONTAS, TIPOVALOR, CAMADA, CONDICAO, CONDICAO_SEQUENCIA, ESQUEMA_DE_CALCULO, PRECO, CONDICAO_CAMADA_ESQUEMA, MERCADORIA, FILIAL, FATURAMENTO, ESTADO, REGION
from rest_framework import serializers

class SEQ_CAMPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEQ_CAMPO
        fields = '__all__'

class SEQUENCIASerializer(serializers.ModelSerializer):
    class Meta:
        model = SEQUENCIA
        fields = '__all__'

class SEQUENCIACAMPOSerializer(serializers.ModelSerializer):
    campos = serializers.SerializerMethodField()

    class Meta:
        model = SEQUENCIA
        fields = '__all__'

    def get_campos(self, obj):
        campos = SEQ_CAMPO.objects.filter(sequencia=obj)
        return SEQ_CAMPOSerializer(campos, many=True).data

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
        fields = '__all__'