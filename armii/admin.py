from django.contrib import admin
from .models import DostawaArmii, LicznikBazowyArmii, LicznikDostawyArmii, DaneStacjiArmii


@admin.register(DaneStacjiArmii)
class DaneStacArmii(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa']


@admin.register(LicznikBazowyArmii)
class LiczBazArmii(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaArmii)
class DostArmiiAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyArmii)
class LiczDostArmiiAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
