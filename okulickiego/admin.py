from django.contrib import admin
from .models import DostawaOkulickiego, LicznikBazowyOkulickiego, LicznikDostawyOkulickiego


@admin.register(LicznikBazowyOkulickiego)
class LiczBazOkuli(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaOkulickiego)
class DostOkuliAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyOkulickiego)
class LiczDostOkuliAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']


