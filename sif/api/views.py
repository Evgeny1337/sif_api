from rest_framework import permissions, viewsets

from .models import DictSection, DictCatalog
from .serializers import DictSectionSerializer, DictCatalogSerializer


class DictSectionViewSet(viewsets.ModelViewSet):
    queryset = DictSection.objects.all()
    serializer_class = DictSectionSerializer

class DictCatalogViewSet(viewsets.ModelViewSet):
    queryset = DictCatalog.objects.all()
    serializer_class = DictCatalogSerializer



