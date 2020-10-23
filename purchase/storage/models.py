from django.db import models

# Create your models here.
class storage(models.Model):
    storage_id = models.AutoField(primary_key=True)
    storage_link = models.URLField()
    storage_name = models.TextField(max_length=255)
    storage_price = models.CharField(max_length=50)
