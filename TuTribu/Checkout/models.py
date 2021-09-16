from django.db import models
from django.db.models.fields import CharField
from Marketplace.models import Producto

# Create your models here.

# Shopping cart


class ShoppingCart(models.Model):
    # usuario =
    orderId = models.Model(CharField=30)
    items = []
    give = models.IntegerField(null=True, blank=True)
    total = 0

class Items(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    itemName = models.ForeignKey(Producto)
    itemID = models.ForeignKey(Producto)
    quantity = models.IntegerField()


class OrderDetail(models.Model):
    pass

class Payment(models.Model):
    pass

