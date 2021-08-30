from django.urls import include
from django.urls import path
from rest_framework import routers

from .views import FieldWorkerViewSet

router = routers.DefaultRouter()
router.register('field-worker', FieldWorkerViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
