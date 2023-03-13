from django.contrib import admin
from .models import DostawaWola, LicznikBazowyWola, LicznikDostawyWola, DaneStacjiWola


@admin.register(DaneStacjiWola)
class DaneStacWola(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa']


@admin.register(LicznikBazowyWola)
class LiczBazWola(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaWola)
class DostWolaAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyWola)
class LiczDostWolaAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
