from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiLezajsk(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowyLezajsk(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaLezajsk(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_lezajsk')


class LicznikDostawyLezajsk(LicznikBaza):
    number = models.ForeignKey(DostawaLezajsk, on_delete=models.CASCADE, related_name='dost_licz_lezajsk')

    def __str__(self):
        return f'{self.number}'
