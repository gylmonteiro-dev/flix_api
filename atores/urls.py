from django.urls import path
from . import views

urlpatterns = [
    path("atores/", views.AtorListCreate.as_view(), name="criar-listar"),
    path("atores/<int:pk>/", views.AtorRetrieveUpdateDestroy.as_view(), name='detalhar-atualizar-deletar')
]
