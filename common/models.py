from django.db import models


class LicznikBaza(models.Model):
    ID_DYS = models.PositiveSmallIntegerField()
    ID_WAZ = models.PositiveSmallIntegerField()
    SYMBOL = models.CharField(max_length=20)
    TOTAL = models.DecimalField(max_digits=30, decimal_places=2)
    ARTYKUL = models.CharField(max_length=250, null=True)
    KIEDY = models.CharField(max_length=150)
    KIEDY_WGR = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Dostawcy(models.Model):
    dostawca = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.dostawca}'


class DostawaAbst(models.Model):
    number = models.PositiveSmallIntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PaliwoDostAbst(DostawaAbst):
    zb_98 = models.DecimalField(max_digits=30, decimal_places=2, default=0, blank=True, null=True)
    zb_95 = models.DecimalField(max_digits=30, decimal_places=2, default=0, blank=True, null=True)
    zb_on = models.DecimalField(max_digits=30, decimal_places=2, default=0, blank=True, null=True)
    zb_ontir = models.DecimalField(max_digits=30, decimal_places=2, default=0, blank=True, null=True)
    zb_lpg = models.DecimalField(max_digits=30, decimal_places=2, default=0, blank=True, null=True)
    zb_adblue = models.DecimalField(max_digits=30, decimal_places=2, default=0, blank=True, null=True)

    class Meta:
        abstract = True
