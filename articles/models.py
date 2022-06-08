from django.db import models

# Create your models here.

class Article(models.Model):
    tilte = models.TextField()
    content = models.TextField()