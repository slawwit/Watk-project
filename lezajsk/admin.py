from django.contrib import admin
from .models import DostawaLezajsk, LicznikBazowyLezajsk, LicznikDostawyLezajsk, DaneStacjiLezajsk


@admin.register(DaneStacjiLezajsk)
class DaneStacLezajsk(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa', 'adress_email']


@admin.register(LicznikBazowyLezajsk)
class LiczBazLezajsk(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaLezajsk)
class DostLezajskAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyLezajsk)
class LiczDostLezajskAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
