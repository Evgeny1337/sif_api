from django.db import models

class DictSection(models.Model):
    """Раздел каталога"""
    name = models.CharField(verbose_name='Название', max_length=100)

    class Meta:
        managed = False
        db_table = 'dict_section'
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name or 'Без названия'


class DictCatalog(models.Model):
    header = models.CharField(verbose_name='Заголовок', max_length=300, blank=True, null=True)
    title = models.CharField(verbose_name='Название', max_length=300, blank=True, null=True)
    author = models.CharField(verbose_name='Автор', max_length=150, blank=True, null=True)
    edition = models.CharField(verbose_name='Издание', max_length=100, blank=True, null=True)
    edition_info = models.CharField(verbose_name='Информация об издании', max_length=100, blank=True, null=True)
    ph_property = models.CharField(verbose_name='Физические свойства', max_length=30, blank=True, null=True)
    section = models.ForeignKey(
        DictSection,
        verbose_name='Раздел',
        on_delete=models.DO_NOTHING,
        db_column='id_section',
        blank=True,
        null=True
    )
    book_num = models.CharField(verbose_name='Номер книги', max_length=30, blank=True, null=True)
    note = models.CharField(verbose_name='Примечание', max_length=100, blank=True, null=True)
    id_directum = models.IntegerField(verbose_name='ID Directum', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dict_catalog'
        verbose_name = 'Книга каталога'
        verbose_name_plural = 'Книги каталога'

    def __str__(self):
        return self.title or self.header or 'Без названия'


class DictBook(models.Model):
    """Экземпляр книги"""
    catalog = models.ForeignKey(
        DictCatalog,
        verbose_name='Каталог',
        on_delete=models.DO_NOTHING,
        db_column='id_catalog',
        related_name='dict_books',
    )
    inv_num = models.CharField(verbose_name='Инвентарный номер', max_length=50, blank=True, null=True)
    serial_num = models.IntegerField(verbose_name='Серийный номер', blank=True, null=True)
    id_directum_catalog = models.IntegerField(verbose_name='ID Directum каталога', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dict_book'
        verbose_name = 'Экземпляр книги'
        verbose_name_plural = 'Экземпляры книг'

    def __str__(self):
        return f"{self.catalog} - {self.inv_num or 'Без номера'}"


class DictCatalogFile(models.Model):
    """Файл каталога"""
    catalog = models.ForeignKey(
        DictCatalog,
        verbose_name='Каталог',
        on_delete=models.DO_NOTHING,
        db_column='id_catalog',
        blank=True,
        null=True
    )
    body = models.BinaryField(verbose_name='Содержимое файла', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dict_catalog_file'
        verbose_name = 'Файл каталога'
        verbose_name_plural = 'Файлы каталога'


class DictEmployee(models.Model):
    """Сотрудник"""
    tab_number = models.IntegerField(verbose_name='Табельный номер', blank=True, null=True)
    first_name = models.CharField(verbose_name='Имя', max_length=50, blank=True, null=True, db_column='firstname')
    second_name = models.CharField(verbose_name='Отчество', max_length=50, blank=True, null=True, db_column='secondname')
    last_name = models.CharField(verbose_name='Фамилия', max_length=50, blank=True, null=True, db_column='lastname')
    filial_name = models.CharField(verbose_name='Филиал', max_length=50, blank=True, null=True)
    dept_name = models.CharField(verbose_name='Отдел', max_length=300, blank=True, null=True)
    post_name = models.CharField(verbose_name='Должность', max_length=300, blank=True, null=True)
    set_date = models.DateTimeField(verbose_name='Дата назначения', blank=True, null=True)
    end_date = models.DateTimeField(verbose_name='Дата окончания', blank=True, null=True)
    email = models.EmailField(verbose_name='Email', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dict_employee'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        full_name = f"{self.last_name or ''} {self.first_name or ''} {self.second_name or ''}".strip()
        return full_name or 'Неизвестный сотрудник'


class DictRole(models.Model):
    """Роль пользователя"""
    name = models.CharField(verbose_name='Название', max_length=30, blank=True, null=True)
    note = models.CharField(verbose_name='Примечание', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dict_role'
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.name or 'Без названия'


class DictUser(models.Model):
    """Пользователь системы"""
    employee = models.ForeignKey(
        DictEmployee,
        verbose_name='Сотрудник',
        on_delete=models.DO_NOTHING,
        db_column='id_employee',
        blank=True,
        null=True
    )
    role = models.ForeignKey(
        DictRole,
        verbose_name='Роль',
        on_delete=models.DO_NOTHING,
        db_column='id_role',
        blank=True,
        null=True
    )
    name = models.CharField(verbose_name='Имя пользователя', max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dict_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name or self.email or 'Неизвестный пользователь'


class DictOrderState(models.Model):
    """Статус заказа"""
    name = models.CharField(verbose_name='Название', max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dict_order_state'
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.name or 'Без названия'


class OrderCatalog(models.Model):
    """Заказ книги"""
    catalog = models.ForeignKey(
        DictCatalog,
        verbose_name='Каталог',
        on_delete=models.DO_NOTHING,
        db_column='id_catalog',
        blank=True,
        null=True
    )
    book = models.ForeignKey(
        DictBook,
        verbose_name='Книга',
        on_delete=models.DO_NOTHING,
        db_column='id_book',
        blank=True,
        null=True
    )
    plan_date = models.DateTimeField(verbose_name='Плановая дата', blank=True, null=True)
    fact_date = models.DateTimeField(verbose_name='Фактическая дата', blank=True, null=True)
    order_date = models.DateTimeField(verbose_name='Дата заказа', blank=True, null=True)
    customer = models.ForeignKey(
        DictEmployee,
        verbose_name='Заказчик',
        on_delete=models.DO_NOTHING,
        db_column='id_customer',
        blank=True,
        null=True
    )
    state = models.ForeignKey(
        DictOrderState,
        verbose_name='Статус',
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        blank=True,
        null=True
    )
    create_date = models.DateTimeField(verbose_name='Дата создания', blank=True, null=True)
    create_user = models.CharField(verbose_name='Создатель', max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_catalog'
        verbose_name = 'Заказ книги'
        verbose_name_plural = 'Заказы книг'

    def __str__(self):
        return f"Заказ {self.id} - {self.catalog}"