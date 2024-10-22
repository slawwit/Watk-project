from django.contrib import admin
from .models import DostawaWarszawska, LicznikBazowyWarszawska, LicznikDostawyWarszawska, DaneStacjiWarszawska


@admin.register(DaneStacjiWarszawska)
class DaneStacWarszawska(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa', 'adress_email']


@admin.register(LicznikBazowyWarszawska)
class LiczBazWarszawska(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaWarszawska)
class DostWarszawskaAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyWarszawska)
class LiczDostWarszawskaAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
