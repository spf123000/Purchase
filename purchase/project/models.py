from django.db import models

# Create your models here.

class project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.TextField(max_length=255)
    project_manager = models.TextField(max_length=50, null=True)
