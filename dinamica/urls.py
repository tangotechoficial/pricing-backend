from rest_framework import routers
from .viewsets import SEQ_CAMPOViewSet, SEQUENCIAViewSet, SEQ_AUXViewSet, CHAVE_CONTASViewSet, TIPOVALORViewSet, CAMADAViewSet, CONDICAOViewSet, CONDICAO_SEQUENCIAViewSet, ESQUEMA_DE_CALCULOViewSet, PRECOViewSet, CONDICAO_CAMADA_ESQUEMAViewSet, MERCADORIAViewSet, FILIALViewSet, FATURAMENTOViewSet, ESTADOViewSet, REGIONViewSet, CONDICAOSEQViewSet, SEQUENCIACAMPOViewSet

router = routers.SimpleRouter()
router.register('seqcampo', SEQ_CAMPOViewSet)
router.register('sequencia', SEQUENCIAViewSet)
router.register('seqaux', SEQ_AUXViewSet)
router.register('chavecontas', CHAVE_CONTASViewSet)
router.register('tipovalor', TIPOVALORViewSet)
router.register('camada', CAMADAViewSet)
router.register('condicao', CONDICAOViewSet)
router.register('condicaosequencia', CONDICAO_SEQUENCIAViewSet)
router.register('esquemadecalculo', ESQUEMA_DE_CALCULOViewSet)
router.register('preco', PRECOViewSet)
router.register('condicaocamadaesquema', CONDICAO_CAMADA_ESQUEMAViewSet)
router.register('mercadoria', MERCADORIAViewSet)
router.register('filial', FILIALViewSet)
router.register('faturamento', FATURAMENTOViewSet)
router.register('estado', ESTADOViewSet)
router.register('region', REGIONViewSet)
router.register('condicaoseq', CONDICAOSEQViewSet)
router.register('sequenciacampo', SEQUENCIACAMPOViewSet)

urlpatterns = router.urls