from rest_framework import routers
from .viewsets import SEQ_CAMPOViewSet, SEQUENCIAViewSet, SEQ_AUXViewSet, CHAVE_CONTASViewSet, TIPOVALORViewSet, CAMADAViewSet, CONDICAOViewSet, CONDICAO_SEQUENCIAViewSet, CONDICAO_CAMADAViewSet, CANAL_VENDASViewSet, LINHA_NEGOCIOViewSet, ESQUEMA_DE_CALCULOViewSet, CAMADA_ESQUEMAViewSet, PRECOViewSet

router = routers.SimpleRouter()
router.register('seqcampo', SEQ_CAMPOViewSet)
router.register('sequencia', SEQUENCIAViewSet)
router.register('seqaux', SEQ_AUXViewSet)
router.register('chavecontas', CHAVE_CONTASViewSet)
router.register('tipovalor', TIPOVALORViewSet)
router.register('camada', CAMADAViewSet)
router.register('condicao', CONDICAOViewSet)
router.register('condicaosequencia', CONDICAO_SEQUENCIAViewSet)
router.register('condicaocamada', CONDICAO_CAMADAViewSet)
router.register('canalvendas', CANAL_VENDASViewSet)
router.register('linhanegocio', LINHA_NEGOCIOViewSet)
router.register('esquemadecalculo', ESQUEMA_DE_CALCULOViewSet)
router.register('camadaesquema', CAMADA_ESQUEMAViewSet)
router.register('preco', PRECOViewSet)

urlpatterns = router.urls