from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.PROTECT)


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
