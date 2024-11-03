from django.urls import path
from . import views


urlpatterns = [
    path(
        "avaliacoes/",
        views.AvaliacaoListCreate.as_view(),
        name="lista-cria-avaliacoes",
    ),
    path(
        "avaliacoes/<int:pk>/",
        views.AvaliacaoRetrieveUpdateDestroy.as_view(),
        name="detalha-atualiza-deleta-avaliacao",
    ),
]
