from django.contrib import admin
from .models import GeneroModel
# Register your models here.


@admin.register(GeneroModel)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'id']


# admin.site.register(Genero)
