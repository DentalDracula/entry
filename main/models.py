from msilib.schema import ServiceControl
from subprocess import check_output
from unicodedata import name
from django.db import models

class Entry(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    service = models.CharField(max_length=350)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    service_man = models.CharField(max_length=250)
    cost = models.IntegerField()

    def __str_(self):
        return self.sno
