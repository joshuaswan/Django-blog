from django.db import models

# Create your models here.

class usertype(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class userinfo(models.Model):
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    emaile =models.EmailField()
    ip = models.GenericIPAddressField()
    memo = models.TextField()
    img = models.ImageField()
    usertype = models.ForeignKey(usertype,null=True,blank=True)