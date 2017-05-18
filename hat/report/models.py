from django.db import models

# Create your models here.
from maintain.models import NodeHierarchy


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    version = models.CharField(max_length=40)
    node_id = models.ForeignKey(NodeHierarchy)