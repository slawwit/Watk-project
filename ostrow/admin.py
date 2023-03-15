from django.contrib import admin
from .models import DostawaOstrow, LicznikBazowyOstrow, LicznikDostawyOstrow, DaneStacjiOstrow


@admin.register(DaneStacjiOstrow)
class DaneStacOstrow(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa']


@admin.register(LicznikBazowyOstrow)
class LiczBazOstrow(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaOstrow)
class DostOstrowAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyOstrow)
class LiczDostOstrowAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
