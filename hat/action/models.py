from django.db import models

# Create your models here.
from maintain.models import TestCase


class TestLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(TestCase)
    time = models.DateTimeField()
    result_choices = (
        (0, "失败"),
        (1, "成功"),
        (2, "无结果"),
    )
    result = models.IntegerField(choices=result_choices, default=0)
    return_data = models.CharField(max_length=500)
