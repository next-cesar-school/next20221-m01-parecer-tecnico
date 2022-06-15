from api.models import Cliente
class ExemploService:
    pass

class ClienteService:
    def criar(self, validated_data):
        print(validated_data)
        cliente = Cliente.objects.create(**validated_data)
        return cliente