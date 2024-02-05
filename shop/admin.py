from django.contrib import admin

# Register your models here.
from .models import Product , Contact, CheckOut,OrderUpdate
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(CheckOut)
admin.site.register(OrderUpdate)