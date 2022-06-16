from api.models import Cliente, Equipamento

class ExemploService:
    pass

class ClienteService:
    def criar(self, validated_data):
        print(validated_data)
        cliente = Cliente.objects.create(**validated_data)
        return cliente

class EquipamentoService:
    def criar(self, validated_data):
        print(validated_data)
        equipamento = Equipamento.objects.create(**validated_data)
        return equipamento