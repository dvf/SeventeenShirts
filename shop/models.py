from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    current_price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category)
    stock = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User)
    product_order = models.ManyToManyField('Order', through='ProductOrder')

    def __unicode__(self):
        return self.pk


class ProductOrder(models.Model):
    SIZES = (
        (u'S', u'Small'),
        (u'M', u'Medium'),
        (u'L', u'Large'),
        (u'XL', u'X-Large'),
    )

    product = models.ForeignKey(Product)
    size = models.CharField(max_length=2, choices=SIZES)

    order = models.ForeignKey(Order)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    create_date = models.DateTimeField(auto_now_add=True)