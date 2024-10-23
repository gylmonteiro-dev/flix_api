import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
# importações do DRF = Django Rest Framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import GeneroModel, AtorModel
from .serializers import GeneroModelSerializer, AtorModelSerializer
# Create your views here.



class GeneroListCreateApiView(ListCreateAPIView):
    queryset = GeneroModel.objects.all()
    serializer_class = GeneroModelSerializer


# View antiga baseada em função para listar e criar
@csrf_exempt
def genero_view(request):

    if request.method == 'GET':
        generos = GeneroModel.objects.all() #Pegando todos os obejtos

        lista_generos = [] # Lista criada 

        for genero in generos:
            lista_generos.append({'id': genero.id, 'nome': genero.nome})

        return JsonResponse(lista_generos, safe=False, status=200)
    
    elif request.method == 'POST':
        # Primeira ação: Receber os dados da requisição
        dados = json.loads(request.body.decode('utf-8'))

        # criar o genero através do modelo
        novo_genero = GeneroModel(nome=dados['nome'])

        # Salvar na base de dados o genero
        novo_genero.save()

        
        return JsonResponse({'id': novo_genero.id, 'nome': novo_genero.nome},status = 201)



# View para Resgatar , atualizar e deletar um dado
class GeneroRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = GeneroModel.objects.all()
    serializer_class = GeneroModelSerializer


@csrf_exempt
def genero_detalhe_view(request, pk):

    genero = get_object_or_404(GeneroModel, pk=pk)

    if request.method == 'GET':
        genero = {'id': genero.id, 'nome': genero.nome}
        return JsonResponse(genero, safe=False, status=200)

    elif request.method == 'DELETE':
        genero.delete()
        return JsonResponse({'msg': 'Recursos deletado com sucesso'}, status=200)

    elif request.method == 'PUT':
        dados = json.loads(request.body.decode("utf-8"))
        genero.nome = dados['nome']
        genero.save()
        return JsonResponse({'id': genero.id, 'nome': genero.nome}, status=201)
    

class AtorListCreateApiView(ListCreateAPIView):
    queryset = AtorModel.objects.all()
    serializer_class = AtorModelSerializer