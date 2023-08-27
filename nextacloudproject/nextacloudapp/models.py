from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length= 100 , null=True , blank= True)
    date_of_birth = models.DateField(null=True , blank=True)
    smart_card_number = models.IntegerField( null=True , blank=True)
    smart_card_colour = models.CharField(max_length=15, null=True, blank=True)
    gender=models.CharField(max_length=15, null=True , blank = True)
    home_address = models.CharField(max_length=100, null=True , blank=True)
    postal_address = models.CharField(max_length=100, null=True , blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    citizenship = models.CharField(max_length=100, null=True, blank=True)
    home_telephone_number= models.IntegerField( null=True, blank=True)
    mobile_number= models.IntegerField( null=True, blank=True)
    email_address = models.EmailField(max_length=200, blank=True, null=True)

class Employers(models.Model):
    name =  models.CharField(max_length= 100 , null=True , blank= True)
    focal_person = models.CharField(max_length= 100 , null=True , blank= True)
    home_address = models.CharField(max_length=100, null=True , blank=True)
    industry = models.CharField(max_length=100, null=True , blank=True)
    description =  models.CharField(max_length=100, null=True , blank=True)