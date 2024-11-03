from django.urls import path
from . import views

urlpatterns = [
    path("filmes/", views.FilmeListCreate.as_view(), name='list-create'),
    path("filmes/<int:pk>/", views.FilmeRetrieveUpdateDestroy.as_view(), name='retrieve-update-destroy')
]
