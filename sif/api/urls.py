from django.urls import include, path
from rest_framework import routers


from .views import DictCatalogViewSet, DictSectionViewSet, DictOrderStateViewSet, DictEmployeeViewSet, DictBookViewSet, \
    DictUserViewSet, DictCatalogFileViewSet, OrderCatalogViewSet, LibraryStateView, DictRoleViewSet, \
    LibraryStateDetailView

router = routers.DefaultRouter()
router.register(r'catalog', DictCatalogViewSet, basename='dictCatalog')
router.register(r'section',DictSectionViewSet, basename='dictSection')
router.register(r'state', DictOrderStateViewSet, basename='dictState')
router.register(r'role', DictRoleViewSet, basename='dictRole')
router.register(r'employee', DictEmployeeViewSet, basename='dictEmployee')
router.register(r'book', DictBookViewSet, basename='dictBook')
router.register(r'user',DictUserViewSet,basename='dictUser')
router.register('file', DictCatalogFileViewSet, basename='catalogfile')
router.register(r'order',OrderCatalogViewSet, basename='ordercatalog')

urlpatterns = [
    path('', include(router.urls)),
    path(r'librarystate/', LibraryStateView.as_view(), name='library_state'),
    path(r'librarystatedetail/', LibraryStateDetailView.as_view(), name='library_state_detail'),
]