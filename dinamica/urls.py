from rest_framework import routers
from .viewsets import CampoViewSet, SequenciaViewSet, TipoValorViewSet, ChaveContasViewSet, CamadaViewSet, CondicaoViewSet, EsquemaDeCalculoViewSet, CondicaoCamadaEsquemaViewSet

router = routers.SimpleRouter()
router.register('campo', CampoViewSet)
router.register('sequencia', SequenciaViewSet)
router.register('tipovalor', TipoValorViewSet)
router.register('chavecontas', ChaveContasViewSet)
router.register('camada', CamadaViewSet)
router.register('condicao', CondicaoViewSet)
router.register('esquemadecalculo', EsquemaDeCalculoViewSet)
router.register('condicaocamadaesquema', CondicaoCamadaEsquemaViewSet)

urlpatterns = router.urls