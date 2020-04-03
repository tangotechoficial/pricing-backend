from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register('movplncmpcal', views.MovplncmpcalViewSet)

urlpatterns = router.urls