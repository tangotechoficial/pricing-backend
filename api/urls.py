from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from . import views

router = routers.DefaultRouter()
router.register(r'dadosmestreverba', views.DadosMestre_VerbaViewSet)
router.register(r'dadosmestreverbacsv', views.DadosMestre_VerbaCSVViewSet)
router.register(r'dadosmestrecomposicao', views.DadosMestre_ComposicaoPrecoViewSet)
router.register(r'dadosmestrecomposicaocsv', views.DadosMestre_ComposicaoPrecoCSVViewSet)
router.register(r'diretrizesestrategica', views.DiretrizesEstrategicaViewSet)
router.register(r'diretrizesestrategicacsv', views.DiretrizesEstrategicaCSVViewSet)
router.register(r'diretrizesestrategicacsv', views.DiretrizesEstrategicaCSVViewSet)
router.register(r'planocompras', views.PlanoComprasViewSet)
router.register(r'otimizador', views.OtimizadorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
]