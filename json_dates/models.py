from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    phone_number = models.IntegerField()
    university = models.CharField(max_length=10)


