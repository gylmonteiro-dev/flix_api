from django.contrib import admin
from .models import Avaliacao

# Register your models here.


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ("filme", "estrelas")
