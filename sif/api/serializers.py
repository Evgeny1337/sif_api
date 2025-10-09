from rest_framework import serializers
from .models import DictUser, DictBook, DictRole, DictSection, DictCatalog, DictEmployee, DictCatalogFile, DictOrderState, OrderCatalog


class DictEmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = DictEmployee
        fields = '__all__'


class DictRoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = DictRole
        fields = ['id', 'name', 'note']

class DictUserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)
    role_id = serializers.IntegerField(write_only=True)
    employee = DictEmployeeSerializer(read_only=True)
    role = DictRoleSerializer(read_only=True)
    class Meta:
        model = DictUser
        fields = ['id', 'name', 'email', 'employee_id', 'role_id', 'employee', 'role']


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

class DictCatalogFileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    catalog_id = serializers.IntegerField(write_only=True)
    catalog = DictCatalogSerializer(read_only=True)
    body = serializers.ImageField()
    class Meta:
        model = DictCatalogFile
        field = ['id','catalog_id', 'catalog', 'body']

class DictBookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    catalog_id = serializers.IntegerField(write_only=True)
    catalog = DictCatalogSerializer(read_only=True)
    class Meta:
        model = DictBook
        field = ['id','catalog_id', 'catalog', 'inv_num','serial_num']

class OrderStateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = DictOrderState
        field = ['id','name']


class OderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    catalog_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)
    catalog = DictCatalogSerializer(read_only=True)
    book = DictBookSerializer(read_only=True)
    pland_date = serializers.DateField()
    fact_date = serializers.DateField()
    order_date = serializers.DateField()
    create_date = serializers.DateTimeField()
    customer_id = serializers.IntegerField(write_only=True)
    customer = DictCatalogSerializer(read_only=True)

    class Meta:
        model = OrderCatalog
        field = ['id', 'catalog_id', 'catalog', 'book_id','book', 'plan_date', 'fact_date', 'order_date', 'create_date', 'customer_id', 'customer']

