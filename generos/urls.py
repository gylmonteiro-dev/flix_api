
from django.urls import path
from .views import  GeneroListCreateApiView, GeneroRetrieveUpdateDestroyApiView

urlpatterns = [
    path("generos/", GeneroListCreateApiView.as_view(), name='lista-generos'),
    path("generos/<int:pk>", GeneroRetrieveUpdateDestroyApiView.as_view(), name="genero_detalha"),

]
