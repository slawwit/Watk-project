from django.db import models
from common.models import LicznikBaza, PaliwoDostAbst, Dostawcy, DaneStacji


class DaneStacjiRzecha(DaneStacji):

    def __str__(self):
        return f'{self.skr_nazwa}'


class LicznikBazowyRzecha(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaRzecha(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_rzecha')


class LicznikDostawyRzecha(LicznikBaza):
    number = models.ForeignKey(DostawaRzecha, on_delete=models.CASCADE, related_name='dost_licz_rzecha')

    def __str__(self):
        return f'{self.number}'
