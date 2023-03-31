from django.contrib import admin
from .models import DostawaPodkarpacka, LicznikBazowyPodkarpacka, LicznikDostawyPodkarpacka, DaneStacjiPodkarpacka


@admin.register(DaneStacjiPodkarpacka)
class DaneStacPodkarpacka(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa']


@admin.register(LicznikBazowyPodkarpacka)
class LiczBazPodkarpacka(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaPodkarpacka)
class DostPodkarpackaAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyPodkarpacka)
class LiczDostPodkarpackaAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
