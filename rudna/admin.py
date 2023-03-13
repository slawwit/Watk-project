from django.contrib import admin
from .models import DostawaRudna, LicznikBazowyRudna, LicznikDostawyRudna, DaneStacjiRudna


@admin.register(DaneStacjiRudna)
class DaneStacRudna(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa']


@admin.register(LicznikBazowyRudna)
class LiczBazRudna(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaRudna)
class DostRudnaAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyRudna)
class LiczDostRudnaAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']


