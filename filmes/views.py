from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Filme
from .serializers import FilmeModelSerializer, FilmeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class FilmeListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Filme.objects.all()
    serializer_class = FilmeModelSerializer


class FilmeRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeModelSerializer