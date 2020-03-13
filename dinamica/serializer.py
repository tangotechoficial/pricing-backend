from .models import SEQ_CAMPO, SEQUENCIA, SEQ_AUX, CHAVE_CONTAS, TIPOVALOR, CAMADA, CONDICAO, CONDICAO_SEQUENCIA, CONDICAO_CAMADA, CANAL_VENDAS, LINHA_NEGOCIO, ESQUEMA_DE_CALCULO, CAMADA_ESQUEMA, PRECO
from rest_framework import serializers

class SEQ_CAMPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEQ_CAMPO
        fields = '__all__'

class SEQUENCIASerializer(serializers.ModelSerializer):
    class Meta:
        model = SEQUENCIA
        fields = '__all__'

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

class CAMADASerializer(serializers.ModelSerializer):
    class Meta:
        model = CAMADA
        fields = '__all__'

class CONDICAOSerializer(serializers.ModelSerializer):
    class Meta:
        model = CONDICAO
        fields = '__all__'

class CONDICAO_SEQUENCIASerializer(serializers.ModelSerializer):
    class Meta:
        model = CONDICAO_SEQUENCIA
        fields = '__all__'

class CONDICAO_CAMADASerializer(serializers.ModelSerializer):
    class Meta:
        model = CONDICAO_CAMADA
        fields = '__all__'

class CANAL_VENDASSerializer(serializers.ModelSerializer):
    class Meta:
        model = CANAL_VENDAS
        fields = '__all__'

class LINHA_NEGOCIOSerializer(serializers.ModelSerializer):
    class Meta:
        model = LINHA_NEGOCIO
        fields = '__all__'

class ESQUEMA_DE_CALCULOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESQUEMA_DE_CALCULO
        fields = '__all__'

class CAMADA_ESQUEMASerializer(serializers.ModelSerializer):
    class Meta:
        model = CAMADA_ESQUEMA
        fields = '__all__'

class PRECOSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRECO
        fields = '__all__'