from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiSikorskiego(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowySikorskiego(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaSikorskiego(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_sikorskiego')


class LicznikDostawySikorskiego(LicznikBaza):
    number = models.ForeignKey(DostawaSikorskiego, on_delete=models.CASCADE, related_name='dost_licz_sikorskiego')

    def __str__(self):
        return f'{self.number}'
