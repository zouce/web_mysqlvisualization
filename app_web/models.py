from django.db import models

class Testtable(models.Model):
    col1 = models.CharField(max_length=256, blank=True)
    col2 = models.CharField(max_length=256, blank=True)
    col3 = models.CharField(max_length=256, blank=True)
    col4 = models.CharField(max_length=256, blank=True)

class Record(models.Model):
    userid = models.IntegerField(blank=True)
    dataurl = models.CharField(max_length=256)

