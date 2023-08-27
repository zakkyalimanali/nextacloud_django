from django.db import models

# Create your models here.

class Brands(models.Model):
    brand_name = models.CharField(max_length=200 , null=True, blank=True)
    type_of_brand = models.CharField(max_length=200 , null=True, blank=True)

class Store(models.Model):
    store_address = models.CharField(max_length=200 , null=True, blank=True)
    store_name = models.CharField(max_length=200 , null=True, blank=True)
    # manager = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank = True)

class Staff(models.Model):
    staff_name = models.CharField(max_length=200, null=True, blank=True)
    staff_position = models.CharField(max_length=200, null=True, blank=True)
    staff_smartcard_number = models.IntegerField(null=True, blank=True)
    staff_smartcard_color = models.CharField(max_length=200, null=True, blank=True)
    staff_date_of_birth = models.DateField(null=True, blank=True)
    joining_date = models.DateField(null=True , blank=True)
    home_address = models.CharField(max_length=100, null=True , blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    citizenship = models.CharField(max_length=100, null=True, blank=True)
    telephone_number= models.IntegerField( null=True, blank=True)
    email_address = models.EmailField(max_length=200, blank=True, null=True)
    mobile_number = models.IntegerField( null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank = True)


    
class Items(models.Model):
    item_name = models.CharField(max_length=200 , null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    # quantity_in_item = models.IntegerField(null=True , blank=True)
    dollar_value = models.IntegerField(null=True, blank=True)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, null=True, blank = True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank = True)
    identification_code = models.CharField(max_length=200 , null=True, blank=True)
    size = models.CharField(max_length=200 , null=True, blank=True)
    country_of_origin = models.CharField(max_length=200 , null=True, blank=True)