from django.db import models

# Create your models here.

# Category(name)
class Category(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

# Supplier(name)
class Supplier(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

# Manufacturer(name)
class Manufacturer(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

# Unit(name)
class Unit(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

# Product(article, name, unit_id, price, supplier_id, manufacturer_id, category_id, discount, amount, description, img)
class Product(models.Model):
    article = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=25)
    unit_id = models.ForeignKey(Unit, on_delete=models.PROTECT)
    price = models.IntegerField()
    supplier_id = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    discount = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return f"{self.article} {self.name.title()}"
