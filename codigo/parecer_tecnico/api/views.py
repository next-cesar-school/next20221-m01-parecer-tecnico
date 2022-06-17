import traceback


from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions, status, serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.serializers import UserSerializer, GroupSerializer, ExemploSerializer, ClienteSerializer, EquipamentoSerializer, ParecerDoTecnico
from api.selectors import ExemploSelector, ClienteSelector, EquipamentoSelector, ParecerDoTecnico
from api.services import ExemploService, ClienteService, EquipamentoService, ParecerDoTecnico

from api.models import Cliente, Equipamento, ParecerDoTecnico
from selectors import ParecerDoTecnicoSelector

from serializers import ParecerDoTecnicoSerializer
from services import ParecerDoTecnicoService



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExemploAPI(GenericAPIView):
    http_method_names = ['get', 'post', 'put', 'delete']
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, exemplo_id=None):
        selector = ExemploSelector()
        exemplo_serializer = None

        if exemplo_id is None:
            exemplos = selector.listar_todos()
            exemplo_serializer = ExemploSerializer(exemplos, many=True)
        else:
            exemplo = selector.buscar_por_id(exemplo_id)

            if exemplo is None:
                return Response(status=status.HTTP_404_NOT_FOUND)

            exemplo_serializer = ExemploSerializer(exemplo)

        return Response(exemplo_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            exemplo_serializer = ExemploSerializer(data=request.data)
            exemplo_serializer.is_valid(raise_exception=True)
            
            exemplo_service = ExemploService()
            exemplo = exemplo_service.criar(exemplo_serializer.data)
            exemplo_serializer_salvo = ExemploSerializer(exemplo)
            
            return Response(exemplo_serializer_salvo.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            print(traceback.format_exc())
            return Response({"msg": "ERROR_DATA_FORMAT"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            print(traceback.format_exc())
            return Response({"msg": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id, format=None):
        pass

    def delete(self, request, id):
        pass
    
class ClienteAPI(GenericAPIView):
    http_method_names = ['get', 'post', 'put', 'delete']
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, cliente_id=None):
        selector = ClienteSelector()
        cliente_serializer = None

        if cliente_id is None:
            clientes = selector.listar_todos()
            cliente_serializer = ClienteSerializer(clientes, many=True)
        else:
            try:
                cliente = selector.buscar_por_id(cliente_id)
                cliente_serializer = ClienteSerializer(cliente)
            except Cliente.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        return Response(cliente_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            cliente_serializer = ClienteSerializer(data=request.data)
            cliente_serializer.is_valid(raise_exception=True)
            
            cliente_service = ClienteService()
            cliente = cliente_service.criar(cliente_serializer.validated_data)
            cliente_serializer_salvo = ClienteSerializer(cliente)
            
            return Response(cliente_serializer_salvo.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            print(traceback.format_exc())
            return Response({"msg": "ERROR_DATA_FORMAT"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            print(traceback.format_exc())
            return Response({"msg": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, cliente_id, format=None):
        print(cliente_id)
        print(request.data)
        cliente_serializer = ClienteSerializer(data=request.data)
        cliente_serializer.is_valid(raise_exception=True)
        cliente = Cliente.objects.get(pk = cliente_id)
        cliente.nomeCompleto = cliente_serializer.validated_data["nomeCompleto"]
        cliente.documentoDeIdentificacao = cliente_serializer.validated_data["documentoDeIdentificacao"]
        cliente.telefone = cliente_serializer.validated_data["telefone"]
        cliente.email = cliente_serializer.validated_data["email"]
        cliente.cep = cliente_serializer.validated_data["cep"]
        cliente.rua = cliente_serializer.validated_data["rua"]
        cliente.localidade = cliente_serializer.validated_data["localidade"]
        cliente.cidade = cliente_serializer.validated_data["cidade"]
        cliente.save()
        cliente_serializer_atualizado = ClienteSerializer(cliente)
        return Response(cliente_serializer_atualizado.data, status=status.HTTP_200_OK)
        

    def delete(self, request, cliente_id):
        try:
            cliente = Cliente.objects.get(pk = cliente_id)
            cliente.delete()
            print("Cliente removido.")
        except:
            print("Cliente não encontrado.")
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EquipamentoAPI(GenericAPIView):
    http_method_names = ['get', 'post', 'put', 'delete']
    
    def get(self, request, equipamentos_id=None):
        selector = EquipamentoSelector()
        equipamento_serializer = None
        
        if equipamentos_id is None:
            equipamentos = selector.listar_todos()
            equipamento_serializer = EquipamentoSerializer(equipamentos, many=True)
        else:
            try:
                equipamento = selector.buscar_por_id(equipamentos_id)
                equipamento_serializer = EquipamentoSerializer(equipamento)
            except Equipamento.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        return Response(equipamento_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        try:
            equipamento_serializer = EquipamentoSerializer(data=request.data)
            equipamento_serializer.is_valid(raise_exception=True)
            
            equipamento_service = EquipamentoService()
            equipamento = equipamento_service.criar(equipamento_serializer.validated_data)
            equipamento_serializer_salvo = EquipamentoSerializer(equipamento)
            
            return Response(equipamento_serializer_salvo.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            print(traceback.format_exc())
            return Response({"msg": "ERROR_DATA_FORMAT"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            print(traceback.format_exc())
            return Response({"msg": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, equipamentos_id, format=None):
        print(equipamentos_id)
        print(request.data)
        equipamento_serializer = EquipamentoSerializer(data=request.data)
        equipamento_serializer.is_valid(raise_exception=True)
        equipamento = Equipamento.objects.get(pk = equipamentos_id)
        equipamento.cliente = equipamento_serializer.validated_data["cliente"]
        equipamento.tipoDeEquipamento = equipamento_serializer.validated_data["tipoDeEquipamento"]
        equipamento.numeroDeSerie = equipamento_serializer.validated_data["numeroDeSerie"]
        equipamento.fabricante = equipamento_serializer.validated_data["fabricante"]
        equipamento.modelo = equipamento_serializer.validated_data["modelo"]
        equipamento.save()
        equipamento_serializer_atualizado = EquipamentoSerializer(equipamento)
        return Response(equipamento_serializer_atualizado.data, status=status.HTTP_200_OK)
    
    def delete(self, request, equipamentos_id):
        try:
            equipamento = Equipamento.objects.get(pk = equipamentos_id)
            equipamento.delete()
            print("Equipamento removido.")
        except:
            print("Equipamento não encontrado.")
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
        
        
class ParecerDoTecnicoAPI(GenericAPIView):
    http_method_names = ['get', 'post', 'put', 'delete']
    
    def get(self, request, ParecerDoTecnicos_id=None):
        selector = ParecerDoTecnicoSelector()
        equipamento_serializer = None
        
        if ParecerDoTecnicos_id is None:
            parecerdotecnicos = selector.listar_todos()
            parecerdotecnicos_serializer = ParecerDoTecnicoSerializer()(parecerdotecnicos, many=True)
        else:
            try:
                parecerdotecnico= selector.buscar_por_id(parecerdotecnicos_id)
                parecerdotecnico_serializer = ParecerDoTecnicoSerializer(parecerdotecnico)
            except ParecerDoTecnico.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        return Response(parecerdotecnico_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        try:
            parecerdotecnico_serializer = ParecerDoTecnicoSerializer(data=request.data)
            parecerdotecnico_serializer.is_valid(raise_exception=True)
            
            parecerdotecnico_service = ParecerDoTecnicoService()
            parecerdotecnico = parecerdotecnico_service.criar(parecerdotecnico_serializer.validated_data)
            parecerdotecnico_serializer_salvo = ParecerDoTecnicoSerializer(parecerdotecnico)
            
            return Response(parecerdotecnico_serializer_salvo.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError:
            print(traceback.format_exc())
            return Response({"msg": "ERROR_DATA_FORMAT"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            print(traceback.format_exc())
            return Response({"msg": "INTERNAL_SERVER_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, parecerdotecnicos_id, format=None):
        
        
        print(parecerdotecnicos_id)
        print(request.data)
        parecerdotecnico_serializer = ParecerDoTecnicoSerializer(data=request.data)
        parecerdotecnico_serializer.is_valid(raise_exception=True)
        parecerdotecnico = ParecerDoTecnico.objects.get(pk = parecerdotecnicos_id)
        
        parecerdotecnico.defeitoRelatado = parecerdotecnico_serializer.validated_data["defeitoRelatado"]
        parecerdotecnico.diagonosticoEfetuado = parecerdotecnico_serializer.validated_data["tdiagonosticoEfetuado"]
        parecerdotecnico.tempoDeReparo = parecerdotecnico_serializer.validated_data["tempoDeReparo"]
        parecerdotecnico.DataDoArquivo= parecerdotecnico_serializer.validated_data["DataDoArquivo"]
        parecerdotecnico.save()
        equipamento_serializer_atualizado = ParecerDoTecnicoSerializer(parecerdotecnico)
        return Response(equipamento_serializer_atualizado.data, status=status.HTTP_200_OK)
    
    def delete(self, request, parecerdotecnicos_id):
        try:
            parecerdotecnico = ParecerDoTecnico.objects.get(pk = parecerdotecnicos_id)
            parecerdotecnico.delete()
            print("Parecer removido.")
        except:
            print("Parecer não encontrado.")
        return Response(status=status.HTTP_204_NO_CONTENT)