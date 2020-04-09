from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('BasePreco', views.BasePrecoViewSet)
router.register('Competitividade', views.CompetitividadeViewSet)
router.register('ElasticidadeDemanda', views.ElasticidadeDemandaViewSet)
router.register('Ettprd', views.EttprdViewSet)
router.register('Ettprdfilter', views.EttprdFilterViewSet)
router.register('Metasdiarias', views.MetasdiariasViewSet)
router.register('Movetq', views.MovetqViewSet)
router.register('Movvbs', views.MovetqViewSet)
router.register('Movvndhstfim', views.MovetqViewSet)
router.register('OutputPln', views.MovetqViewSet)
router.register('Prdsml', views.MovetqViewSet)
router.register('movplncmpcal', views.MovplncmpcalViewSet)
router.register('dadosmestreverba', views.DadosMestre_VerbaViewSet)
router.register('elasticidade', views.ElasticidadeViewSet)
router.register('verbaebc', views.VerbaeBCViewSet)
router.register('vendas', views.VendasViewSet)
router.register('dadosmestrecomposicao', views.DadosMestre_ComposicaoPrecoViewSet)
router.register('diretrizesestrategicas', views.DiretrizesEstrategicaViewSet)
router.register(r'planocompras', views.PlanoComprasViewSet)


urlpatterns = router.urls