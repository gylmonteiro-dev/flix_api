from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Ator
from .serializers import AtorSerializer
# Create your views here.


class AtorListCreate(ListCreateAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer


class AtorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer