from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    current_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return self.name


class Order(models.Model):
    SIZES = (
        (u'S', u'Small'),
        (u'M', u'Medium'),
        (u'L', u'Large'),
        (u'XL', u'X-Large'),
    )

    customer = models.ForeignKey(User)
    product = models.ForeignKey(Product)

    size = models.CharField(max_length=2, choices=SIZES)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{0}".format(self.customer.username)