from django.db import models
from django.contrib.auth.models import User


class Entity(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва об'єкту")

    class Meta:
        verbose_name = "Об'єкт"
        verbose_name_plural = "Об'єкти"

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Працівник"
        verbose_name_plural = "Працівники"    


class Category(models.Model):
    category_name = models.CharField(
        max_length=200, verbose_name="Назва категорії")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def __str__(self):
        return self.category_name


class Product(models.Model):
    DIMENSIONS = (
        ('шт.', 'шт.'),
        ('кг.', 'кг.'),
    )

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    code = models.IntegerField(primary_key=True, verbose_name="Артикул")
    product_name = models.CharField(
        max_length=200, verbose_name="Назва продукту")
    unit = models.CharField(max_length=5, choices=DIMENSIONS)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

    def __str__(self):
        return self.product_name


class Document(models.Model):
    document_name = models.CharField(
        max_length=100, verbose_name="Назва документу")
    user = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    create_data = models.DateTimeField(auto_now_add=True)
    change_data = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документи"


class DocumentLines(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=4, decimal_places=2, default=0)
