from django.db.models import Count, F, Value
from django.db.models.functions import Concat
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

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


#Отчеты
class LibraryStateView(APIView):
    #Добавить проверки на ошибки
    def get(self, request):
        catalog_with_books = DictCatalog.objects.select_related('section').annotate(
            books_count=Count('dict_books'),
            section_name=F('section__name'),
        ).distinct()

        data = list(catalog_with_books.values(
            'pk',
            'title',
            'author',
            'section_name',
            'books_count',
            'header',
        ))
        return Response(data)

class LibraryStateDetailView(APIView):
    # Добавить проверки на ошибки
    def get(self, request):
        catalog_id = request.GET.get('id')
        order_books = (OrderCatalog.objects.filter(catalog_id=catalog_id)
                       .select_related('book','state')
                       .annotate(
                            book_num = F('book__inv_num'),
                            state_name = F('state__name'),
                            customer_fio = Concat(
                    F('customer__last_name'), Value(' '),
                                F('customer__first_name'), Value(' '),
                                F('customer__second_name')
                            )
                        )
                       ).distinct()
        data = list(order_books.values(
     'book_num',
            'state_name',
            'customer_fio',
            'plan_date',
            'fact_date'
        ))
        return Response(data)





