from django.urls import include, path
from rest_framework import routers

from .views import DictCatalogViewSet, DictSectionViewSet

router = routers.DefaultRouter()
router.register(r'catalog', DictCatalogViewSet)
router.register(r'section',DictSectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]