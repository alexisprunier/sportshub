from django.db import models
from django.contrib import admin

class Article(models.Model):
    titre = models.CharField(max_length=150, unique=True)
    contenu = models.TextField(null=True)
    origine = models.CharField(max_length=42)
    type = models.CharField(max_length=10)
    lien = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de parution")
    image = models.CharField(max_length=200)
    sport = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.titre