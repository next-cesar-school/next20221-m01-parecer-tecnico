import traceback

from django.shortcuts import render
from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions, status, serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.serializers import UserSerializer, GroupSerializer, ExemploSerializer
from api.selectors import ExemploSelector
from api.services import ExemploService

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
