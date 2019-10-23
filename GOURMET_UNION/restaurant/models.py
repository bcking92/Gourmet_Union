from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    score = models.FloatField(default=0)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    business_hour_mon = models.CharField(max_length=30)
    business_hour_tue = models.CharField(max_length=30)
    business_hour_wed = models.CharField(max_length=30)
    business_hour_tur = models.CharField(max_length=30)
    business_hour_fri= models.CharField(max_length=30)
    business_hour_sat = models.CharField(max_length=30)
    business_hour_sun = models.CharField(max_length=30)
    