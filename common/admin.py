from django.contrib import admin
from .models import Dostawcy
# Register your models here.


@admin.register(Dostawcy)
class DostawcyOkuli(admin.ModelAdmin):
    list_display = ['dostawca']
