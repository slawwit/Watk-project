from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiArmii(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowyArmii(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaArmii(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_armii')


class LicznikDostawyArmii(LicznikBaza):
    number = models.ForeignKey(DostawaArmii, on_delete=models.CASCADE, related_name='dost_licz_armii')

    def __str__(self):
        return f'{self.number}'
