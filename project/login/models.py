from django.db import models


# Create your models here.
class sqlserverconn(models.Model):
    admin_id = models.IntegerField(max_length=15)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=25)
