from django.db import models
from common.models import LicznikBaza, DostawaAbst, PaliwoDostAbst, Dostawcy


class LicznikBazowyOkulickiego(LicznikBaza):

    def __str__(self):
        return f'{self.ARTYKUL}'


class DostawaOkulickiego(PaliwoDostAbst):
    dostawca = models.ForeignKey(Dostawcy, on_delete=models.CASCADE, related_name='dost_okuli')


class LicznikDostawyOkulickiego(LicznikBaza):
    number = models.ForeignKey(DostawaOkulickiego, on_delete=models.CASCADE, related_name='dost_licz_okuli')

    def __str__(self):
        return f'{self.number}'
