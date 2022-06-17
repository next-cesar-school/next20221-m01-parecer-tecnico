from api.models import Cliente, Equipamento, ParecerDoTecnico
class ExemploSelector:
    def listar_todos(self):
        # como buscar todos do banco de dados?
        pass

    def buscar_por_id(self, id):
        # como buscar somente um registro/objeto do banco de dados?
        pass
    
class ClienteSelector:
    def listar_todos(self):
        # como buscar todos do banco de dados?
        return Cliente.objects.all()
        

    def buscar_por_id(self, id):
        # como buscar somente um registro/objeto do banco de dados?
        return Cliente.objects.get(pk=id)

class EquipamentoSelector:
    def listar_todos(self):
        # como buscar todos do banco de dados?
        return Equipamento.objects.all()
    
    def buscar_por_id(self, id):
        # como buscar somente um registro/objeto do banco de dados?
        return Equipamento.objects.get(pk=id)
       
class ParecerDoTecnicoSelector:
    def listar_todos(self):
        # como buscar todos do banco de dados?
        return ParecerDoTecnico.objects.all()
    
    def buscar_por_id(self, id):
        # como buscar somente um registro/objeto do banco de dados?
        return ParecerDoTecnico.objects.get(pk=id)
