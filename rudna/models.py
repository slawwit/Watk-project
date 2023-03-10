from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiRudna(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowyRudna(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaRudna(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_rudna')


class LicznikDostawyRudna(LicznikBaza):
    number = models.ForeignKey(DostawaRudna, on_delete=models.CASCADE, related_name='dost_licz_rudna')

    def __str__(self):
        return f'{self.number}'
