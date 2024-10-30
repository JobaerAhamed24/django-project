from django.db import models

# Create your models here.
class Service(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    sort_description = models.CharField(max_length=500)
    
class About(models.Model):
    main_title = models.CharField(max_length= 50)
    sort_description = models.CharField( max_length=500)
    title = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    website_link = models.URLField(max_length=1000)
    phone = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField()
    Degree = models.CharField(max_length=50)
    email = models.EmailField( max_length=100)

class Socile(models.Model):
    link = models.URLField(max_length=200)
    link_icon = models.CharField(max_length=100)
    
