from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=500,blank=False,null=False,error_messages={
            "required": 'name is required..',
        })
    price = models.FloatField(blank=False,null=False,error_messages={
            "required": 'price is required..',
        })
    quantity = models.IntegerField(blank=False,null=False,error_messages={
            "required": 'quantity is required..',
        })