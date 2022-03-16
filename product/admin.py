from django.contrib import admin

# Register your models here.
from .models import product, brand,customer,product_category,UserLogin

admin.site.register(product)
admin.site.register(brand)
admin.site.register(customer)
admin.site.register(product_category)
admin.site.register(UserLogin)