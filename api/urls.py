from django.conf.urls import include, url 
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from . import views

router = routers.DefaultRouter()
router.register(r'fornecedor', views.FornecedorViewSet)
router.register(r'comprador', views.CompradorViewSet)
router.register(r'tabauxgrp', views.TabAuxGrpViewSet)
router.register(r'relacionamentofilial', views.RelacionamentoFilialRegiaoViewSet)
router.register(r'mercadoria', views.MercadoriaViewSet)
router.register(r'representante', views.RepresentanteViewSet)
router.register(r'vendas', views.VendasViewSet)
router.register(r'verbaebc', views.VerbaeBCViewSet)
router.register(r'elasticidade', views.ElasticidadeViewSet)
router.register(r'estoque', views.EstoqueViewSet)
router.register(r'competitividade', views.CompetitividadeViewSet)
router.register(r'dadosmestreverba', views.DadosMestre_VerbaViewSet)
router.register(r'dadosmestreverbacsv', views.DadosMestre_VerbaCSVViewSet)
router.register(r'dadosmestrecomposicao', views.DadosMestre_ComposicaoPrecoViewSet)
router.register(r'dadosmestrecomposicaocsv', views.DadosMestre_ComposicaoPrecoCSVViewSet)
router.register(r'diretrizesestrategica', views.DiretrizesEstrategicaViewSet)
router.register(r'diretrizesestrategicacsv', views.DiretrizesEstrategicaCSVViewSet)
router.register(r'planocompras', views.PlanoComprasViewSet)
router.register(r'otimizador', views.OtimizadorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
]