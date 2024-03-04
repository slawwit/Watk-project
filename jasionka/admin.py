from django.contrib import admin
from .models import DostawaJasionka, LicznikBazowyJasionka, LicznikDostawyJasionka, DaneStacjiJasionka


@admin.register(DaneStacjiJasionka)
class DaneStacJasionka(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa', 'adress_email']


@admin.register(LicznikBazowyJasionka)
class LiczBazJasionka(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaJasionka)
class DostJasionkaAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyJasionka)
class LiczDostJasionkaAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
