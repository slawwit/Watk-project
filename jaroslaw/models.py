from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiJaroslaw(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowyJaroslaw(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaJaroslaw(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_jaroslaw')


class LicznikDostawyJaroslaw(LicznikBaza):
    number = models.ForeignKey(DostawaJaroslaw, on_delete=models.CASCADE, related_name='dost_licz_jaroslaw')

    def __str__(self):
        return f'{self.number}'
