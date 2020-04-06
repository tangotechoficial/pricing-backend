from rest_framework import routers
from .viewsets import CampoViewSet, SequenciaViewSet, TipoValorViewSet, ChaveContasViewSet, CamadaViewSet, CondicaoViewSet, EsquemaDeCalculoViewSet, CondicaoCamadaEsquemaViewSet, SequenciaCondicaoViewSet, FilialExpedicaoViewSet, FilialFaturamentoViewSet, RegiaoViewSet, EstadoViewSet, MercadoriaViewSet, ChavePrecificaoViewSet, PrecoViewSet, EsquemaRelationViewSet, CodterchvCodcnlViewSet

router = routers.SimpleRouter()
router.register('campo', CampoViewSet)
router.register('sequencia', SequenciaViewSet)
router.register('tipovalor', TipoValorViewSet)
router.register('chavecontas', ChaveContasViewSet)
router.register('camada', CamadaViewSet)
router.register('condicao', CondicaoViewSet)
router.register('esquemadecalculo', EsquemaDeCalculoViewSet)
router.register('condicaocamadaesquema', CondicaoCamadaEsquemaViewSet)
router.register('sequenciacondicao', SequenciaCondicaoViewSet)
router.register('filialexpedicao', FilialExpedicaoViewSet)
router.register('filialfaturamento', FilialFaturamentoViewSet)
router.register('regiao', RegiaoViewSet)
router.register('estado', EstadoViewSet)
router.register('productos', MercadoriaViewSet)
router.register('chaveprecificaos', ChavePrecificaoViewSet)
router.register('preco', PrecoViewSet)
router.register('esquemarelations', EsquemaRelationViewSet)
router.register('codterchvcodcnl', CodterchvCodcnlViewSet)

urlpatterns = router.urls