from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiWarszawska(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowyWarszawska(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaWarszawska(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_warszawska')


class LicznikDostawyWarszawska(LicznikBaza):
    number = models.ForeignKey(DostawaWarszawska, on_delete=models.CASCADE, related_name='dost_licz_warszawska')

    def __str__(self):
        return f'{self.number}'
