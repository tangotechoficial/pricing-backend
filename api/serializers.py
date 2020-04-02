from rest_framework import serializers

from django.contrib.auth.models import User

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'is_superuser', 'username',
                  'first_name', 'last_name', 'email', 'groups')


class FornecedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Fornecedor
        fields = ('CODDIVFRN', 'DESDIVFRN', 'CODGRPECOFRN', 'NOMGRPECOFRN')


class CompradorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Comprador
        fields = ("CODCPR", "NOMCPR", "CODDIVCMP",
                  "DESDIVCMP", "CODDRTCLLATU", "DESDRTCLLATU")


class TabAuxGrpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TabAuxGrp
        fields = ("Id_Aux", "CODCLSMER", "DESCLSMER", "CODFMLMER",
                  "DESGRPMER", "CODGRPMER", "DESGRPMER", "Linha_de_negocio")


class RelacionamentoFilialRegiaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RelacionamentoFilialRegiao
        fields = ("CODFILEPD", "NOMFILEPD", "CODFILFAT", "NOMFILFAT",
                  "CODESTUNI", "NOMESTUNI", "TIPEDEREG", "CODEDEREG")


class MercadoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Mercadoria
        fields = ("CODPRD", "Id_Aux", "DESPRD", "CODDIVFRN",
                  "CODCPRATU", "CODSML", "dessml", "ABC")


class RepresentanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Representante
        fields = ("CODREPCMC", "NOMREPCMC", "DATCADREPCMC")


class VendasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Vendas
        fields = ("CODPRD", "CODFILEPD", "CODFILFAT", "CODESTCLI", "CODREPCMC", "NUMPED", "NUMANOMESSMN", "NUMANOMESDIA", "VLRVNDLIQ", "QDEITE", "VLRDSCFLXCNS",
                  "VLRSUPFLX", "VLRIMPTOT", "VLRRCTLIQAPU", "VLRCSTMEDPRD", "PERMRGADICNLVND", "VLRFND", "VLRMRGBRT", "VLRCSTTRNTNLCUB", "VLRCSTDTB", "VLRCSTARG", "VLRMRGCRB")


class VerbaeBCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VerbaeBC
        fields = ("CODPRD", "CODFILEPD", "CODFILFAT", "CODECLI", "CODESTCLI", "NUMANOMESDIA", "QDEITEPED", "VLRVNDLIQ", "VLRUNTCSTMER", "VLRCSTMER", "VLRUNTFNDMER", "VLRFND", "QDEITEPMC",
                  "QDEITEBFC", "VLRUNTFNDPMCVND", "VLRUNTDSCBFCITE", "VLRUNTFNDPCO", "VLRUNTFNDMRG", "VLRRLZPMC", "VLRBFC", "VLRFNDPCOVND", "VLRFNDPCOCST", "VLRMNSFNDRCBFRN", "VLRRBTCAL")


class ElasticidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Elasticidade
        fields = ("CODPRD", "CODESTUNI", "CODFILEPD", "CODFILFAT", "VLRVARVNDPCO",
                  "DESMER", "CLFCRVABCMER", "CODGRPMERSMR", "DESGRPMERSMR")


class EstoqueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Estoque
        fields = ("CODPRD", "CODFILEPD", "DATREF", "NUMSMNANO", "NOMDIASMN", "NOMMESANO", "NOMSMSANO", "NOMABVMESANO", "VLRUNTCSTSCO", "QDEITEETQ", "VLRVNDPDAFLTETQ", "VLRCSTCMPIDL", "VLRMEDPCOCMP", "CODSTAPRDETQ")


class CompetitividadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.Competitividade
        fields=("CODPRD", "COCODIDTCUR", "CODESTUNI", "CODESTUNIOR", "CODESTUNIDS", "NUMANO", "NUMANOMES", "NUMSMNANO",
                "NOMMES", "DATREF", "CODSML", "DESGRPMERSMR", "CODTIPAPU", "VLRPCOMEDMCD", "VLRPCOBSEMER", "CLFCRVABCMER", "CODDIVFRN")


class DadosMestre_VerbaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.DadosMestre_Verba
        fields=("CODPRD", "CODSMLPCO", "CODFILEPD", "DATREF", "VLRSLDPCOMESANT",
                "VLRCRDPCO", "VLRDBTPCO", "VLRSLDMRGMESANT", "VLRCRDMRG", "VLRCRDMRG")




class DadosMestre_VerbaCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.DadosMestre_VerbaCSV
        fields=['import_date']


class DadosMestre_ComposicaoPrecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.DadosMestre_ComposicaoPreco
        fields=("CODPRD", "CODFILEPD", "CODFILFAT", "DATREF", "CODESTUNI", "TIPEDEREG", "VLRMRGBRT", "VLRVBA", "VLRFND", "VLRFNDRBTITE", "VLRICM", "VLRPIS",
                "VLRDVL", "VLRUNTPCOALV", "VLRFLXCNS", "VLRCSTCAL", "VLRBNF", "VLRCPLCSTPCO", "VLRPCOBSEMER", "CODREGPCO", "NUMRLCCIDGIR", "TIPCALUTZPCOLIQ")


class DadosMestre_ComposicaoPrecoCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.DadosMestre_ComposicaoPrecoCSV
        fields=['import_date']


class DiretrizesEstrategicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.DiretrizesEstrategica
        fields=("CODESTUNI", "CODDIVFRN", "DATREFPOD", "NOMMES", "NOMSMS", "NOMDIASMN", "NOMSMSANO", "CODUNDNGCCLI", "CODCLLCMPATU", "DESDRTCLLATU",
                "CODSGMNGCCLI", "VLRVNDFATLIQ", "VLRRCTLIQAPU", "VLRMRGCRB", "VLRMRGBRT", "NOMCPR", "CODFIL", "CODCLSMER", "DESCLSMER", "CODFMLMER", "DESGRPMER", "CODGRPMER", "DESGRPMER", "DESDIVFRN", "CODGRPECOFRN", "NOMGRPECOFRN")


class DiretrizesEstrategicaCSVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.DiretrizesEstrategicaCSV
        fields=['import_date']


class PlanoComprasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.PlanoCompras
        fields=("CODPRD", "CODFILEPD", "CODFILFAT", "CODESTUNI", "MONTH", "YEAR", "WEEK", "OLVNDSUG", "VOLVNDSUGALC", "MRGBRTPEROCD", "VLRPCOSUG", "VLRPCOBASESUG", 
                  "VLRIMPTOTSUG", "VLRICMSSUG", "VLRPISCOFSUG", "VLRDEVSUG", "VLRFLXSUG", "VLRMRGBRTSUG", "VRBUNTSUGSUG", "VLRVRBPLAN", "VLRCMVPCOSUG", "VLRCMVPCOATU", "VLRCMVCMPATU", "VOLVNDPLN", "MRGBRTPEROCD", "VLRPCOPLN", "VLRPCOBASEPLN", "VLRIMPTOTPLN", "VLRICMSPLN", "VLRPISCOFPLN", "VLRDEVPLN", "VLRFLXPLN", "VLRMRGBRTPLN", "VRBUNTSUGPLN", "VLRVRBPLN", "VLRCMVPCOPLN", "VLRCMVCMPPLN")


class OtimizadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.Otimizador
        fields=("DATREF", "CODEFILEPD", "CODFILFAT", "CODPRD",
                "VLRVBA", "VLRVBADIS", "VLRVBAINP", "VLRVBACAL", "VLRVBADEM")
