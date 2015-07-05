from django.contrib import admin
from shop.models import *


admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Category)