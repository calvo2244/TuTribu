from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Company(models.Model):
    pass


class Store(models.Model):
    storeName = models.CharField(max_length=50)
    purposeType = models.ManyToManyField()
    businessAddress = models.CharField(max_length=40)
    #setName
    #getName


class Category(models.Model):
    toTribe = models.ManyToManyField()
    

class Product(models.Model):
    productName = CharField(max_length=50)
    productID = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category)
    stock = models.FloatField()
    productImage= models.ImageField()

    #addProduct
    #editProduct
    #deleteProduct
    #postProduct
    #setPrice
    #editStock
    



