from django.contrib import admin
from .models import ExternalSite, Litre, Product, Group, ProductLiters, ProductPage
# Register your models here.
admin.site.register(ExternalSite)
admin.site.register(Product)
admin.site.register(Litre)
admin.site.register(Group)
admin.site.register(ProductLiters)
admin.site.register(ProductPage)

