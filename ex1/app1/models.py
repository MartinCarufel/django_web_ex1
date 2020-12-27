from django.db import models

# Create your models here.

class MyData(models.Model):
    nom = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self):
        return(self.nom)

