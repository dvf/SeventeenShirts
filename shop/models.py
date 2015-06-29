from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    current_price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category)


class Customer(models.Model):
    user = models.OneToOneField(User)


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    product_order = models.ManyToManyField('Order', through='ProductOrder')


class ProductOrder(models.Model):
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    create_date = models.DateTimeField(auto_now_add=True)



