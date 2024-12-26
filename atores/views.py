from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Ator
from .serializers import AtorSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class AtorListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer


class AtorRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer