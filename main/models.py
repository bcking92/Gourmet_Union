from django.db import models

# Create your models here.
class Food_info(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.FloatField()
    address = models.TextField()
    food_type = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    service_time = models.TextField()
    description = models.TextField()

class Rate_info(models.Model):
    restaurant_id = models.IntegerField()
    user_id = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    picture = models.FileField()

class User_info(models.Model):
    user_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    