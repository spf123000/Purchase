from django.db import models

# Create your models here.
class commodity(models.Model):
    commodity_serial = models.AutoField(primary_key=True)
    commodity_id = models.CharField(max_length=50)
    commodity_link = models.URLField()
    commodity_name = models.TextField(max_length=255)
    commodity_price = models.CharField(max_length=50)
