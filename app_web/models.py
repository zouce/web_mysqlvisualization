from django.db import models

class Testtable(models.Model):
    col1 = models.CharField(max_length=256, blank=True)
    col2 = models.CharField(max_length=256, blank=True)
    col3 = models.CharField(max_length=256, blank=True)
    col4 = models.CharField(max_length=256, blank=True)

class Record(models.Model):
    userid = models.IntegerField(blank=True)
    dataurl = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)

class HIGGS(models.Model):
    col1 = models.FloatField(blank=True)
    col2 = models.FloatField(blank=True)
    col3 = models.FloatField(blank=True)
    col4 = models.FloatField(blank=True)
    col5 = models.FloatField(blank=True)
    col6 = models.FloatField(blank=True)
    col7 = models.FloatField(blank=True)
    col8 = models.FloatField(blank=True)
    col9 = models.FloatField(blank=True)
    col10 = models.FloatField(blank=True)
    col11 = models.FloatField(blank=True)
    col12 = models.FloatField(blank=True)
    col13 = models.FloatField(blank=True)
    col14 = models.FloatField(blank=True)
    col15 = models.FloatField(blank=True)
    col16 = models.FloatField(blank=True)
    col17 = models.FloatField(blank=True)
    col18 = models.FloatField(blank=True)
    col19 = models.FloatField(blank=True)
    col20 = models.FloatField(blank=True)
    col21 = models.FloatField(blank=True)
    col22 = models.FloatField(blank=True)
    col23 = models.FloatField(blank=True)
    col24 = models.FloatField(blank=True)
    col25 = models.FloatField(blank=True)
    col26 = models.FloatField(blank=True)
    col27 = models.FloatField(blank=True)
    col28 = models.FloatField(blank=True)
    col29 = models.FloatField(blank=True)
