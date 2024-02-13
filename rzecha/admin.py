from django.contrib import admin
from .models import DostawaRzecha, LicznikBazowyRzecha, LicznikDostawyRzecha, DaneStacjiRzecha


@admin.register(DaneStacjiRzecha)
class DaneStacRzecha(admin.ModelAdmin):
    list_display = ['skr_nazwa', 'nazwa', 'adress_email']


@admin.register(LicznikBazowyRzecha)
class LiczBazRzecha(admin.ModelAdmin):
    list_display = ['id', 'ID_DYS', 'SYMBOL', 'KIEDY', 'KIEDY_WGR']


@admin.register(DostawaRzecha)
class DostRzechaAdmin(admin.ModelAdmin):
    list_display = ['number', 'created', 'modified']


@admin.register(LicznikDostawyRzecha)
class LiczDostRzechaAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
