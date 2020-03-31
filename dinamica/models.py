from django.db import models
class SEQ_CAMPO(models.Model):
    Cod_Campo = models.CharField(max_length=10, primary_key=True)
    Nome_Campo = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Nome_Campo

class SEQUENCIA(models.Model):
    Cod_Sequencia = models.CharField(max_length=10, primary_key=True)
    Nome_Sequencia = models.CharField(max_length=50, unique=True)
    campos = models.ManyToManyField(SEQ_CAMPO)

    def __str__(self):
        return self.Nome_Sequencia

class SEQ_AUX(models.Model):
    Cod_Sequencia = models.ForeignKey(SEQUENCIA, on_delete=models.CASCADE)
    Cod_Campo = models.ForeignKey(SEQ_CAMPO, on_delete=models.CASCADE)

class CHAVE_CONTAS(models.Model):
    Cod_ChaveContas = models.CharField(max_length=10, primary_key=True)
    Desc_ChaveContas = models.CharField(max_length=50)

    def __str__(self):
        return self.Desc_ChaveContas

class TIPOVALOR(models.Model):
    Cod_TipoValor = models.CharField(max_length=10, primary_key=True)
    Desc_TipoValor = models.CharField(max_length=50)

    def __str__(self):
        return self.Desc_TipoValor

class CAMADA(models.Model):
    Cod_Camada = models.CharField(max_length=10, primary_key=True)
    Nome_Camada = models.CharField(max_length=50)
    TIPO_BASE_VENDAS = models.CharField(max_length=1)

    def __str__(self):
        return self.Nome_Camada

class CONDICAO(models.Model):
    Cod_Condicao = models.CharField(max_length=10, primary_key=True)
    Desc_Condicao = models.CharField(max_length=50)
    Cod_Camada = models.ForeignKey(CAMADA, on_delete=models.CASCADE)
    Cod_ChaveContas = models.ForeignKey(CHAVE_CONTAS, on_delete=models.CASCADE)
    Cod_TipoValor = models.ForeignKey(TIPOVALOR, on_delete=models.CASCADE)
    Escala_Qtde = models.IntegerField()
    POS_NEG = models.CharField(max_length=1)
    TIP_BASE_VENDAS = models.CharField(max_length=1)
    MANDATORIA = models.IntegerField()  
    ESTATISTICA = models.IntegerField()
    sequencias = models.ManyToManyField(SEQUENCIA)
    value = models.TextField(null=True)

    def __str__(self):
        return self.Desc_Condicao

class CONDICAO_SEQUENCIA(models.Model):
    Cod_Condicao = models.ForeignKey(CONDICAO, on_delete=models.CASCADE)
    Cod_Sequencia = models.ForeignKey(SEQUENCIA, on_delete=models.CASCADE)

class ESQUEMA_DE_CALCULO(models.Model):
    Cod_Esquema_Calculo = models.CharField(max_length=10, primary_key=True)
    TIP_BASE_VENDAS = models.CharField(max_length=1)

class PRECO(models.Model):
    Chave = models.IntegerField()
    Data = models.DateTimeField()
    Cod_Esquema_Calculo = models.ForeignKey(ESQUEMA_DE_CALCULO, on_delete=models.CASCADE)
    Valor = models.FloatField()
    Tipo_Base_Venda = models.CharField(max_length=1)

class CONDICAO_CAMADA_ESQUEMA(models.Model):
    Cod_Condicao = models.ForeignKey(CONDICAO, on_delete=models.CASCADE)
    Cod_Camada = models.ForeignKey(CAMADA, on_delete=models.CASCADE)
    Cod_Esquema_Calculo = models.ForeignKey(ESQUEMA_DE_CALCULO, on_delete=models.CASCADE)

class MERCADORIA(models.Model):
    DESTIPCRT = models.CharField(max_length=3)
    CODPRD = models.CharField(max_length=10)
    DESPRD = models.CharField(max_length=50)
    CODGRPPRD = models.CharField(max_length=10)
    CODCLSPRD = models.CharField(max_length=10)
    DESCLSPRD = models.CharField(max_length=50)
    CODSUBCTGPRD = models.CharField(max_length=5)
    DESSUBCTGPRD = models.CharField(max_length=50)
    CODSMR = models.IntegerField()
    DESSMR = models.CharField(max_length=50)

class ESTADO(models.Model):
    Cod_Estado = models.CharField(max_length=2, primary_key=True)
    Desc_Estado = models.CharField(max_length=50)

class FILIAL(models.Model):
    Cod_Filial = models.IntegerField()
    Desc_Filial = models.CharField(max_length=50)
    Cod_Faturamento = models.CharField(max_length=10)
    Cod_Estado = models.ForeignKey(ESTADO, on_delete=models.CASCADE)

class FATURAMENTO(models.Model):
    Cod_Faturamento = models.CharField(max_length=10, primary_key=True)
    Desc_Faturamento = models.CharField(max_length=50)
    Cod_Filial = models.ForeignKey(FILIAL, on_delete=models.CASCADE)

class REGION(models.Model):
    Cod_Region = models.CharField(max_length=10, primary_key=True)
    Tipo_Region = models.CharField(max_length=50)
    Cod_Estado = models.ForeignKey(ESTADO, on_delete=models.CASCADE)

class FILIAL_MERCADORIA(models.Model):
    Cod_Filial_Mercadoria = models.CharField(max_length=20, primary_key=True)
    Cod_Filial = models.ForeignKey(FILIAL, on_delete=models.CASCADE)
    Cod_Faturamento = models.ForeignKey(FATURAMENTO, on_delete=models.CASCADE)
    Cod_Estado = models.ForeignKey(ESTADO, on_delete=models.CASCADE)
    Cod_Region = models.ForeignKey(REGION, on_delete=models.CASCADE)
    Tipo_Region = models.IntegerField()
    id_Mercadoria = models.ForeignKey(MERCADORIA, on_delete=models.CASCADE)

class ESQUEMA_FILIAL_MERCADORIA(models.Model):
    Cod_Esquema_Calculo = models.ForeignKey(ESQUEMA_DE_CALCULO, on_delete=models.CASCADE)
    Cod_Filial_Mercadoria = models.ForeignKey(FILIAL_MERCADORIA, on_delete=models.CASCADE)