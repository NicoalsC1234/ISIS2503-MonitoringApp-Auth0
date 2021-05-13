from django.db import models

class Boletin(models.Model):
    name = models.CharField(max_length=50)
    materia = models.CharField(max_length=50)
    nota = models.FloatField(max_length=10)

    def __str__(self):
        return '{}'.format(self.name)

