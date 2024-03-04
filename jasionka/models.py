from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiJasionka(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowyJasionka(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaJasionka(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_jasionka')


class LicznikDostawyJasionka(LicznikBaza):
    number = models.ForeignKey(DostawaJasionka, on_delete=models.CASCADE, related_name='dost_licz_jasionka')

    def __str__(self):
        return f'{self.number}'
