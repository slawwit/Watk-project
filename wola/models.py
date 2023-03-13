from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiWola(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowyWola(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaWola(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_wola')


class LicznikDostawyWola(LicznikBaza):
    number = models.ForeignKey(DostawaWola, on_delete=models.CASCADE, related_name='dost_licz_wola')

    def __str__(self):
        return f'{self.number}'
