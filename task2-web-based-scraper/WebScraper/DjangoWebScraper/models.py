from django.db import models

# Create your models here.
class Link(models.Model):
    scraped_link=models.CharField(max_length=5000)