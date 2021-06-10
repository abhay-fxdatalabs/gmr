from django.db import models
from django.db import models

class God(models.Model):
    date =models.DateField()
    planned_srldc = models.IntegerField()
    forced_srldc = models.IntegerField()
    total_Outage_srldc = models.IntegerField()
    planned_nrldc = models.IntegerField()
    forced_nrldc = models.IntegerField()
    total_Outage_nrldc = models.IntegerField()
    planned_erldc = models.IntegerField()
    forced_erldc = models.IntegerField()
    total_Outage_erldc = models.IntegerField()
    planned_wrldc = models.IntegerField()
    forced_wrldc = models.IntegerField()
    total_Outage_wrldc = models.IntegerField()

class Iex(models.Model):
    date = models.DateField()
    time_Block = models.CharField(max_length=20)
    mcp = models.FloatField()
    mcv = models.FloatField()
    purchase_Bid = models.FloatField()
    sell_Bid = models.FloatField()
    cleared_Volume = models.FloatField()
    final_Scheduled_Volume = models.FloatField()

class Psp(models.Model):
    date = models.DateField()
    availability_erldc = models.FloatField()
    demand_Met_erldc = models.FloatField()
    shortage_erldc = models.FloatField()
    availability_nrldc = models.FloatField
    demand_Met_nrldc = models.FloatField
    shortage_nrldc = models.FloatField
    availability_srldc = models.FloatField
    demand_Met_srldc = models.FloatField
    shortage_srldc = models.FloatField
    availability_wrldc = models.FloatField
    demand_Met_wrldc = models.FloatField
    shortage_wrldc = models.FloatField

class Dsm(models.Model):
    date = models.DateField()
    freq_below = models.FloatField()
    freq_not_below = models.FloatField()
    A1 = models.FloatField()
    A2 = models.FloatField()
    E1 = models.FloatField()
    E2 = models.FloatField()
    N1 = models.FloatField()
    N2 = models.FloatField()
    N3 = models.FloatField()
    S1 = models.FloatField()
    S2 = models.FloatField()
    S3 = models.FloatField()
    W1 = models.FloatField()
    W2 = models.FloatField()
    W3 = models.FloatField()
    inter_regional = models.FloatField()
