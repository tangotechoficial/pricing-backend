from django.db import models

class SEQ_CAMPO(models.Model):
    Cod_Campo = models.CharField(max_length=10, unique=True)
    Nome_Campo = models.CharField(max_length=50, unique=True)

class SEQUENCIA(models.Model):
    Cod_Sequencia = models.CharField(max_length=10, unique=True)
    Nome_Sequencia = models.CharField(max_length=50, unique=True)

class SEQ_AUX(models.Model):
    id_Sequencia = models.ForeignKey(SEQUENCIA, on_delete=models.CASCADE)
    id_Campo = models.ForeignKey(SEQ_CAMPO, on_delete=models.CASCADE)

class CHAVE_CONTAS(models.Model):
    Cod_ChaveContas = models.CharField(max_length=10, unique=True)
    Desc_ChaveContas = models.CharField(max_length=50)

class TIPOVALOR(models.Model):
    Cod_TipoValor = models.CharField(max_length=10, unique=True)
    Desc_TipoValor = models.CharField(max_length=50)

class CAMADA(models.Model):
    Cod_Camada = models.CharField(max_length=10, unique=True)
    Nome_Camada = models.CharField(max_length=50)
    TIPO_BASE_VENDAS = models.CharField(max_length=1)

class CONDICAO(models.Model):
    Cod_Condicao = models.CharField(max_length=10, unique=True)
    Desc_Condicao = models.CharField(max_length=50)
    id_Camada = models.ForeignKey(CAMADA, on_delete=models.CASCADE)
    id_ChaveContas = models.ForeignKey(CHAVE_CONTAS, on_delete=models.CASCADE)
    id_TipoValor = models.ForeignKey(TIPOVALOR, on_delete=models.CASCADE)
    Escala_Qtde = models.IntegerField()
    POS_NEG = models.CharField(max_length=1)
    TIP_BASE_VENDAS = models.CharField(max_length=1)
    MANDATORIA = models.IntegerField()
    ESTATISTICA = models.IntegerField()

class CONDICAO_SEQUENCIA(models.Model):
    id_Condicao = models.ForeignKey(CONDICAO, on_delete=models.CASCADE)
    id_Sequencia = models.ForeignKey(SEQUENCIA, on_delete=models.CASCADE)

class CONDICAO_CAMADA(models.Model):
    id_Condicao = models.ForeignKey(CONDICAO, on_delete=models.CASCADE)
    id_Camada = models.ForeignKey(CAMADA, on_delete=models.CASCADE)

class CANAL_VENDAS(models.Model):
    Cod_Vendas = models.CharField(max_length=10)
    Desc_Vendas = models.CharField(max_length=50)

class LINHA_NEGOCIO(models.Model):
    Cod_LinhaNegocio = models.CharField(max_length=10)
    Desc_LinhaNegocio = models.CharField(max_length=50)

class ESQUEMA_DE_CALCULO(models.Model):  
    id_CanalVendas = models.ForeignKey(CANAL_VENDAS, on_delete=models.CASCADE)
    id_LinhaNegocio = models.ForeignKey(LINHA_NEGOCIO, on_delete=models.CASCADE)

class CAMADA_ESQUEMA(models.Model):
    id_Condicao_Camada = models.ForeignKey(CONDICAO_CAMADA, on_delete=models.CASCADE)
    id_Esquema = models.ForeignKey(ESQUEMA_DE_CALCULO, on_delete=models.CASCADE)

class PRECO(models.Model):
    Chave = models.IntegerField()
    Data = models.DateTimeField()
    id_Esquema_Calculo = models.ForeignKey(ESQUEMA_DE_CALCULO, on_delete=models.CASCADE)
    Valor = models.FloatField()
    Tipo_Base_Venda = models.CharField(max_length=1)
