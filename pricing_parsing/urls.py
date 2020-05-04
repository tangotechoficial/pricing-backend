from django.conf.urls import include, url 
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register('BasePreco', views.BasePrecoViewSet)
router.register('Competitividade', views.CompetitividadeViewSet)
router.register('ElasticidadeDemanda', views.ElasticidadeDemandaViewSet)
router.register('Ettprd', views.EttprdViewSet)
router.register('Metasdiarias', views.MetasdiariasViewSet)
router.register('Movetq', views.MovetqViewSet)
router.register('Movvbs', views.MovetqViewSet)
router.register('Movvndhstfim', views.MovetqViewSet)
router.register('OutputPln', views.MovetqViewSet)
router.register('Prdsml', views.MovetqViewSet)
router.register('movplncmpcal', views.MovplncmpcalViewSet)

urlpatterns = router.urls