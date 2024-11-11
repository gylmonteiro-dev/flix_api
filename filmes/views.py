from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Filme
from .serializers import FilmeModelSerializer, FilmeSerializer
# Create your views here.


class FilmeListCreate(ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


class FilmeRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeModelSerializer