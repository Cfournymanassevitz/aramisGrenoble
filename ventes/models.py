from django.db import models

from .utils import get_agency_names


class Vente(models.Model):
    agence = models.CharField(max_length=200)
    nb_ventes = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.agence} - {self.nb_ventes} - {self.date}'
