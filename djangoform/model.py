from __future__ import unicode_literals
from django.db import models


class StudeMobilis(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(max_length=5)
    date = models.DateField


class Meta:
    db_table = "student"
