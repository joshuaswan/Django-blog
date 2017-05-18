from django.db import models


# Create your models here.

class Gander(models.Model):
    name = models.CharField(max_length=32)


class UserType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    nid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    emaile = models.EmailField()
    ip = models.GenericIPAddressField()
    memo = models.TextField()
    img = models.ImageField()
    usertype = models.ForeignKey(UserType, null=True, blank=True)
    gender_choice = (
        (0, 'man'),
        (1, 'weman'),
    )
    gender = models.IntegerField(choices=gender_choice, default=1)


class Boy(models.Model):
    name = models.CharField(max_length=32)


class Girl(models.Model):
    name = models.CharField(max_length=32)
    f = models.ManyToManyField(Boy)


class B2G(models.Model):
    boy = models.ForeignKey(Boy)
    girl = models.ForeignKey(Girl)
