from django.contrib.gis.db import models

# Create your models here.
class Students(models.Model):
    """docstring here"""
    name = models.CharField(max_length=40)
    gpa = models.CharField(max_length=4)
    address = models.CharField(max_length=200)

    def __str__(self):
        return"{}".format(self.name)

