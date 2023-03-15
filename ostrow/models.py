from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiOstrow(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowyOstrow(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaOstrow(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_ostrow')


class LicznikDostawyOstrow(LicznikBaza):
    number = models.ForeignKey(DostawaOstrow, on_delete=models.CASCADE, related_name='dost_licz_ostrow')

    def __str__(self):
        return f'{self.number}'
