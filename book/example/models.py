from django.db import models


class Author(models.Model):
    name=models.CharField(max_length=100)


class Authoring(models.Model):
    collaboration_type=models.CharField(max_length=100)
    book=models.ForeignKey(Book)
    author = models.ForeignKey(Author)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author,through=Authoring)

