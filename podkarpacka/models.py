from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiPodkarpacka(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowyPodkarpacka(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaPodkarpacka(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_podkarpacka')


class LicznikDostawyPodkarpacka(LicznikBaza):
    number = models.ForeignKey(DostawaPodkarpacka, on_delete=models.CASCADE, related_name='dost_licz_podkarpacka')

    def __str__(self):
        return f'{self.number}'
