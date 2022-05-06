from django.db import models
from PIL import Image
# Create your models here.
class ExternalSite(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="uploads/")
    description = models.TextField()
    link = models.CharField(max_length=255, verbose_name="Website Link")
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        if self.logo:
            return self.logo.url
        else:
            return  None
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
    
class Litre(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="name")
    price = models.FloatField()
    amount_of_litres = models.CharField(max_length=20)
    
    def save(self, *args, **kwargs):
        self.price = round(self.price, 2)
        super(Litre, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.product.name
    


#individual product pages
class Group(models.Model):
    category = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category
    
class ProductLiters(models.Model):
    liters = models.CharField(max_length=50)
    
    def __str__(self):
        return self.liters
    
class ProductPage(models.Model):
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE, null=False, verbose_name="category")
    productliters = models.ForeignKey(to=ProductLiters, on_delete=models.CASCADE, null=False, verbose_name="liters")
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return  None