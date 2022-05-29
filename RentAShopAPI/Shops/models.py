from django.db import models

# Create your models here.
class ShopImage(models.Model):
    image = models.ImageField(upload_to="shop_images")
    
class Shop(models.Model):
    owner = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()
    number = models.BigIntegerField()
    area = models.BigIntegerField()
    deposit = models.BigIntegerField()
    rent = models.BigIntegerField()
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    images = models.ManyToManyField(ShopImage)

    def __str__(self):
        return self.address
