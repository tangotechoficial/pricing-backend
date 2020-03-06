from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from . import views

router = routers.DefaultRouter()
router.register(r'dadosmestre', views.DadosMestreViewSet)
router.register(r'dadosmestrecsv', views.DadosMestreCSVViewSet)
router.register(r'diretrizesestrategica', views.DiretrizesEstrategicaViewSet)
router.register(r'diretrizesestrategicacsv', views.DiretrizesEstrategicaCSVViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/', obtain_jwt_token),
]