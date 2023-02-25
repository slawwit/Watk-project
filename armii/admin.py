from django.contrib import admin
from .models import DostawaArmii, LicznikBazowyArmii, LicznikDostawyArmii


@admin.register(LicznikBazowyArmii)
class LiczBazArmii(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaArmii)
class DostArmiiAdmin(admin.ModelAdmin):
    list_display = ['number', 'created']


@admin.register(LicznikDostawyArmii)
class LiczDostArmiiAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
