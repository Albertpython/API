from django.db import models

# Create your models here.
class Auto(models.Model):
    name = models.CharField('Name auto', max_length=60)
    mark = models.CharField('Name mark', max_length=60)

    def __str__(self):
        return self.name



