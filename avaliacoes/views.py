from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Avaliacao
from .serializers import AvaliacaoSerializer
# Create your views here.


class AvaliacaoListCreate(ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class AvaliacaoRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
