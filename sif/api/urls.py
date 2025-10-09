from django.urls import include, path
from rest_framework import routers

from .serializers import DictRoleSerializer
from .views import DictCatalogViewSet, DictSectionViewSet, DictOrderStateViewSet, DictEmployeeViewSet, DictBookViewSet, \
    DictUserViewSet, DictCatalogFileViewSet, OrderCatalogViewSet

router = routers.DefaultRouter()
router.register(r'catalog', DictCatalogViewSet)
router.register(r'section',DictSectionViewSet)
router.register(r'state', DictOrderStateViewSet)
router.register(r'role', DictRoleSerializer)
router.register(r'employee', DictEmployeeViewSet)
router.register(r'book', DictBookViewSet)
router.register(r'user',DictUserViewSet)
router.register('file', DictCatalogFileViewSet)
router.register(r'order',OrderCatalogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]