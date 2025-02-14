from django.db import models

# Create your models here.
class shopdetails(models.Model):
    shopname = models.CharField(max_length=100)
    shoplocation = models.CharField(max_length=100)
    shopcategory = models.CharField(max_length=50)
    shopdescription= models.TextField(max_length=200)


class manageoffers(models.Model):
    offershopname = models.CharField(max_length=100)
    offershoplocation = models.CharField(max_length=100)
    offercategory = models.CharField(max_length=50)
    offertitle = models.CharField(max_length=50)
    offerdescription= models.TextField(max_length=200)  
    offerstartdate=models.DateField()
    offerenddate=  models.DateField()

class categoryfloor(models.Model):
    category = models.CharField(max_length=50)
    floor = models.IntegerField()




    