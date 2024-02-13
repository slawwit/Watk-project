from django.contrib import admin
from .models import DostawaSikorskiego, LicznikBazowySikorskiego, LicznikDostawySikorskiego, DaneStacjiSikorskiego


@admin.register(DaneStacjiSikorskiego)
class DaneStacSikorskiego(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa', 'adress_email']


@admin.register(LicznikBazowySikorskiego)
class LiczBazSikorskiego(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaSikorskiego)
class DostSikorskiegoAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawySikorskiego)
class LiczDostSikorskiegoAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
