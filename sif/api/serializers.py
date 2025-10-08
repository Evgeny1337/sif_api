from rest_framework import serializers
from .models import DictUser, DictBook, DictRole, DictSection, DictCatalog, DictEmployee, DictCatalogFile, DictOrderState, OrderCatalog, DatabaseChangeLog, DatabaseChangeLogLock


class DictSectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = DictSection
        fields = ['id','name']

class DictCatalogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    section_id = serializers.IntegerField(write_only=True)
    section_name = DictSectionSerializer(read_only=True)
    class Meta:
        model = DictCatalog
        fields = ['id','header', 'title', 'author', 'edition', 'edition_info', 'ph_property', 'section_id', 'section_name']

