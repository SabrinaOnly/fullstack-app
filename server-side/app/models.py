from django.db import models

class Record(models.Model):
    name = models.CharField(max_length=40)
    tel = models.CharField(max_length=12)