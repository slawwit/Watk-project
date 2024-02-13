from django.contrib import admin
from .models import DostawaJaroslaw, LicznikBazowyJaroslaw, LicznikDostawyJaroslaw, DaneStacjiJaroslaw


@admin.register(DaneStacjiJaroslaw)
class DaneStacJaroslaw(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa', 'adress_email']


@admin.register(LicznikBazowyJaroslaw)
class LiczBazJaroslaw(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaJaroslaw)
class DostJaroslawAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyJaroslaw)
class LiczDostJaroslawAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
