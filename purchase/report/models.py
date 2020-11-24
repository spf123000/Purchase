from django.db import models

# Create your models here.
class report(models.Model):
    report_serial = models.AutoField(primary_key=True)
    report_id = models.CharField(max_length=50)
    report_link = models.URLField()
    report_name = models.TextField(max_length=255)
    report_num = models.IntegerField(blank=True, null=True, default=1)
    report_price = models.FloatField()
    report_total = models.FloatField(blank=True, null=True)
    report_project = models.TextField(max_length=255)
    # report_spending = 
