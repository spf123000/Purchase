from django.db import models
from project.models import project

# Create your models here.
class commodity(models.Model):
    commodity_serial = models.AutoField(primary_key=True)
    commodity_id = models.CharField(max_length=50)
    commodity_link = models.URLField()
    commodity_name = models.TextField(max_length=255)
    commodity_num = models.IntegerField(blank=True, null=True, default=1)
    commodity_price = models.FloatField()
    commodity_total = models.FloatField(blank=True, null=True)
