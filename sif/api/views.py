from rest_framework import permissions, viewsets

from .models import DictSection, DictCatalog, DictBook, DictUser, DictRole, DictEmployee, OrderCatalog, DictOrderState
from .serializers import DictSectionSerializer, DictCatalogSerializer, DictBookSerializer, DictUserSerializer, \
    DictRoleSerializer, DictEmployeeSerializer, DictCatalogFileSerializer, OrderStateSerializer


class DictSectionViewSet(viewsets.ModelViewSet):
    queryset = DictSection.objects.all()
    serializer_class = DictSectionSerializer

class DictCatalogViewSet(viewsets.ModelViewSet):
    queryset = DictCatalog.objects.all()
    serializer_class = DictCatalogSerializer

class DictBookViewSet(viewsets.ModelViewSet):
    queryset = DictBook.objects.all()
    serializer_class = DictBookSerializer

class DictUserViewSet(viewsets.ModelViewSet):
    queryset = DictUser.objects.all()
    serializer_class = DictUserSerializer

class DictRoleViewSet(viewsets.ModelViewSet):
    queryset = DictRole.objects.all()
    serializer_class = DictRoleSerializer

class DictEmployeeViewSet(viewsets.ModelViewSet):
    queryset = DictEmployee.objects.all()
    serializer_class = DictEmployeeSerializer

class DictCatalogFileViewSet(viewsets.ModelViewSet):
    queryset = DictCatalog.objects.all()
    serializer_class = DictCatalogFileSerializer

class OrderCatalogViewSet(viewsets.ModelViewSet):
    queryset = OrderCatalog.objects.all()
    serializer_class = DictCatalogFileSerializer

class DictOrderStateViewSet(viewsets.ModelViewSet):
    queryset = DictOrderState.objects.all()
    serializer_class = OrderStateSerializer





